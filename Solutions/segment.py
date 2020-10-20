import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage.io import imread
import numpy as np
from skimage.color import rgb2yuv
from skimage.filters import sobel
import cv2


def segment():
    def nothing(x):
        pass
    cv2.namedWindow('bars')
    cv2.createTrackbar('h_l', 'bars', 0, 180, nothing)
    cv2.createTrackbar('s_l', 'bars', 0, 255, nothing)
    cv2.createTrackbar('v_l', 'bars', 0, 255, nothing)
    cv2.createTrackbar('h_u', 'bars', 0, 180, nothing)
    cv2.createTrackbar('s_u', 'bars', 0, 255, nothing)
    cv2.createTrackbar('v_u', 'bars', 0, 255, nothing)
    cap = cv2.VideoCapture(0)
    lower = {'o': (0,70,130), 'y':(25, 100, 100),'g':(45,70,70), 'b': (100,100,0)}
    upper = {'o': (10,255,255), 'y':(40,255,255), 'g':(100,255,255), 'b': (130,255,255)}
    s = False
    while True:
        _, frame = cap.read()
        
        if s:
            filtered = cv2.GaussianBlur(frame, (5,5), 1) 
            hsv = cv2.cvtColor(filtered, cv2.COLOR_BGR2HSV)
            ll = (cv2.getTrackbarPos('h_l', 'bars'),cv2.getTrackbarPos('s_l', 'bars'),cv2.getTrackbarPos('v_l', 'bars'))
            uu = (cv2.getTrackbarPos('h_u', 'bars'),cv2.getTrackbarPos('s_u', 'bars'),cv2.getTrackbarPos('v_u', 'bars'))
            mask = cv2.inRange(hsv, ll, uu)
            frame[mask==0]=0

        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)
        if k== -1:
            continue
        if chr(k) == 's':
            s = not s
        if chr(k) in 'ogby':
            l = lower[chr(k)]
            u = upper[chr(k)]
            cv2.setTrackbarPos('h_l', 'bars', l[0])
            cv2.setTrackbarPos('s_l', 'bars', l[1])
            cv2.setTrackbarPos('v_l', 'bars', l[2])
            cv2.setTrackbarPos('h_u', 'bars', u[0])
            cv2.setTrackbarPos('s_u', 'bars', u[1])
            cv2.setTrackbarPos('v_u', 'bars', u[2])


        if k == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()