from PIL import Image
import numpy as np
import doctest


def get_color(matrix, x_start, y_start, gradation):
    """

    :param matrix: матрица
    :param x_start: начальные положения x
    :param y_start: и y
    :param gradation: количество градаций серого цвета,
    :return: возвращает значение серого цвета, которое после используется
          для формирования изображения в методе make_mosaic
    >>> get_color([[[1, 2, 3]]], 0, 0, 1)
    2
    >>> get_color([[[0, 0, 0]]], 0, 0, 1)
    0
    >>> get_color([[[50, 100, 150]] * 3] * 3, 0, 0, 3)
    100
    """
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
    """

    :param matrix: основная матрица
    :param x_start: начальные положения x и y
    :param y_start: -
    :param gradation: степень градации серого цвета, используется для расчета переменной gray
    :param grey: основной параметр серого цвета.
    :param gray_gradation: Вводимое с клавиатуры значение, обозначает градацию серого цвета
    (50 как коэффициент, можно убрать, но я не вижу причин)
    :return: возвращает двумерный массив, по которому формируется результативное изображение
    >>> get_matrix([[[100, 120, 140]]], 0, 0, 1, 120, 50)
    [[[100, 100, 100]]]
    """
    grey_gradations = gray_gradation * 50
    for x in range(x_start, x_start + gradation):
        for y in range(y_start, y_start + gradation):
            matrix[x][y] = [int(grey // grey_gradations) * grey_gradations] * 3


def make_mosaic(img, gradation, grey_gradation):
    """

    :param img: исходное изображение
    :param gradation: шаг обработки
    :param grey_gradation: водимое с клавиатуры значение, обозначает градацию серого цвета
    :return: формирует картинку из массива matrix
    """
    matrix = np.array(img)
    height = len(matrix)
    width = len(matrix[1])
    for x in range(0, height - 1, gradation):
        for y in range(0, width - 1, gradation):
            grey = get_color(matrix, x, y, gradation)
            get_matrix(matrix, x, y, gradation, grey, grey_gradation)
    return Image.fromarray(matrix)


def main():
    """

    :return: ничего не возвращает, просто сохраняет изображение в формате jpg
    """
    print('Введите название исходного изображения:')
    img = Image.open(input())
    print(
        "Введите степень пикселизации изображения  серого цвета:")
    gradation = int(input())
    print("Введите степень градации серого цвета")
    grey_gradation = int(input())
    res = make_mosaic(img, gradation, grey_gradation)
    res.save('res.jpg')
    doctest.testmod()


if __name__ == '__main__':
    main()
