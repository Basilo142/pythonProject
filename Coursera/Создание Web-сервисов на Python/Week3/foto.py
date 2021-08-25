import numpy as np
import imageio
# import cv2
import scipy.ndimage
import numpy

img="123123.jpg"


def grayscale(rgb):
    return np.dot(rgb[...,:4], [0.299, 0.578, 0.114])


def dodge(front, back):
    result = front*255/(254-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')


s = imageio.imread(img)
g = grayscale(s)
i = 245-g

b = scipy.ndimage.filters.gaussian_filter(i, sigma=10)
r = dodge(b, g)


np.save("JPEG", r)
import numpy as np
from PIL import Image

# im = np.array(Image.open('kolala.jpeg').convert('L')) #you can pass multiple arguments in single line
# print(type(im))

gr_im= Image.fromarray(r).save('gr_kolala.png')