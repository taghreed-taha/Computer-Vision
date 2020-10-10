'''
Import here most important libraries
'''

def zero_channel(image, channel):
     """ Return image **excluding** the rgb channel specified
    Args:
        image: numpy array of shape(image_height, image_width, 3)
        channel: number specifying the channel (0 for B, 1 for G, 2 for R)
    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """


def draw_solid_square_slow(image, x, y, l, color):
    """ Returns image after drawing a square on the image using python nested loops
    Args:
        image: numpy array of shape(image_height, image_width, 3)
        (x,y): a tuple specifying upper left corner
        l: square edge length
        color: a tuple specifying (B,G,R)
    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """


def draw_solid_square_fast(image, x, y, l, color):
    """ Returns image after drawing a square on the image using numpy arrays operations
    Args:
        image: numpy array of shape(image_height, image_width, 3)
        (x,y): a tuple specifying upper left corner
        l: square edge length
        color: a tuple specifying (B,G,R)
    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """



def combine_images_h(img1, img2):
    """ Return 2 images combined horizontally. If the heights of images are different, you
    may set additional space to black
Args:
    img1: numpy array of shape(image_height, image_width, 3)
    img2: numpy array of shape(image_height, image_width, 3)
Returns:
    out: numpy array
""" 

def combine_images_v(img1, img2):
    """ Return 2 images combined vetically. If the widths of images are different, you
    may set additional space to black
Args:
    img1: numpy array of shape(image_height, image_width, 3)
    img2: numpy array of shape(image_height, image_width, 3)
Returns:
    out: numpy array
"""

def my_bgr2gray(image):
    """
    Returns a grayscale image where each pixel value = (B+G+R)/3
Args:
    image: numpy array of shape(image_height, image_width, 3)
Returns:
    out: numpy array of shape(image_height, image_width, 3)
"""

def normalize_img(image):
    """
    normalize each channel independently according to the following formula
    pixel = (channel_value - channel_mean)/channel_std
Args:
    image: numpy array of shape(image_height, image_width, 3)
Returns:
    out: numpy array of shape(image_height, image_width, 3)
"""