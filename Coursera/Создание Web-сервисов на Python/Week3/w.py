import numpy as np
import imageio
import cv2
import scipy.ndimage
import numpy

img = "1231.jpg"
img = "123.jpg"
qwe = cv2.imread(img)
wwwww=1

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.578, 0.114])


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

gr_im= Image.fromarray(r).save('1231-2.png')


img = s


def edge_mask(img, line_size, blur_value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
    return edges


line_size = 9
blur_value = 5

edges = edge_mask(img, line_size, blur_value)
a=1
gr_im2= Image.fromarray(edges).save('1231-3.png')


def color_quantization(img, k):
# Преобразуем изображение
    data = np.float32(img).reshape((-1, 3))

# Задаем критерии
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Внедряем метод k-средних
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result


total_color = 15
img = color_quantization(img, total_color)

gr_im2= Image.fromarray(img).save('1231-4.png')


blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200,sigmaSpace=200)
cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)
gr_im2= Image.fromarray(blurred).save('1231-5.png')
gr_im2= Image.fromarray(cartoon).save('1231-6.png')

