import numpy as np

def zero_channel(image, channel):
    out = image.copy()
    out[:,:,channel] = 0    
    return out


def draw_solid_square_slow(image, x, y, l, color):
    H,W = image.shape[:2]
    out = image.copy()
    for i in range(y, min(y+l,H)):
        for j in range(x, min(x+l, W)):
            out[i,j] = np.array(color)
    return out

def draw_solid_square_fast(image, x, y, l, color):
    H, W = image.shape[:2]
    out = image.copy()
    out[y:min(y+l,H), x:min(x+l,W)] = np.array(color)
    return out



def combine_images_h(img1, img2):
    H1, W1 = img1.shape[:2]
    H2, W2 = img2.shape[:2]
    out = np.zeros((max(H1, H2), W1+W2, 3))
    out[:H1, :W1] = img1.copy()
    out[:H2, W1:W1+W2] = img2.copy()
    return out.astype(np.uint8)

def combine_images_v(img1, img2):
    H1, W1 = img1.shape[:2]
    H2, W2 = img2.shape[:2]
    out = np.zeros((H1 + H2, max(W1, W2), 3))
    out[:H1, :W1] = img1.copy()
    out[H1:H1+H2, :W2] = img2.copy()
    return out.astype(np.uint8)


def my_bgr2gray(image):
    out = np.sum(image, axis=2)/3
    return (out).astype(np.uint8)

def normalize_img(image):
    means = [np.mean(image[:,:,i]) for i in range(3)]
    stds = [np.std(image[:,:,i]) for i in range(3)]

    return (image - means)//stds