import numpy as np
import imageio
import cv2
import scipy.ndimage
import numpy

img = "123.jpg"
qwe = cv2.imread(img)
wwwww=1
def read_file(name):

    img = cv2.imread(name)
    a=23
    # cv2_imshow(img)
    return img


def color_quantization(img, k):
# Transform the image
    data = np.float32(img).reshape((-1, 3))

# Determine criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementing K-Means
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result


def edge_mask(img, line_size, blur_value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
    return edges

name = "123123.jpg"


img = read_file(name)
imgg = cv2.imread(name)
a=1
