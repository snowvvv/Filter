from PIL import Image
import numpy as np


def get_color(matrix, x_start, y_start, gradation):
    grey = 0
    for x in range(x_start, x_start + gradation):
        for y in range(y_start, y_start + gradation):
            r = int(matrix[x][y][0])
            g = int(matrix[x][y][1])
            b = int(matrix[x][y][2])
            grey += (r + g + b) / 3  # расчет серого цвета
    grey = int(grey // (gradation ** 2))
    return grey


def get_matrix(matrix, x_start, y_start, gradation, grey, gray_gradation):
    grey_gradations = gray_gradation * 50
    for x in range(x_start, x_start + gradation):
        for y in range(y_start, y_start + gradation):
            matrix[x][y] = [int(grey // grey_gradations) * grey_gradations] * 3


def make_mosaic(img, gradation, grey_gradation):
    matrix = np.array(img)
    height = len(matrix)
    width = len(matrix[1])
    for x in range(0, height - 1, gradation):
        for y in range(0, width - 1, gradation):
            grey = get_color(matrix, x, y, gradation)
            get_matrix(matrix, x, y, gradation, grey, grey_gradation)
    return Image.fromarray(matrix)


def main():
    img = Image.open("img2.jpg")                                        #размер блока (чем больше шаг, тем сильнее пикселизация)
    gradation = 10
    grey_gradation = 1                                               #степень градации серого цвета, 1= эталон
    res = make_mosaic(img, gradation, grey_gradation)
    res.save('res.jpg')


if __name__ == '__main__':
    main()
