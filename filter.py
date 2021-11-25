from PIL import Image
import numpy as np


def get_area_average(arr, start_row, start_col, width, height):
    """
    Return average value of area. Sizes of area are in cell_size

    :param arr: array
    :param start_row: int
    :param start_col: int
    :param width: int
    :param height: int
    :return: float

    >>> get_area_average([[[100, 100, 100], [200, 200, 200]], [[200, 200, 200], [100, 100, 100]]], 0, 0, 2, 2)
    450
    """
    average = 0
    for row in range(start_row, start_row + height):
        for col in range(start_col, start_col + height):
            for i in range(3):
                average += int(arr[row][col][0])
    average = int(average // (width * height))
    return average


def change_area_color(arr, start_row, start_col, average, width, height, step):
    """
    Change pixels for average in area
    :param arr: array
    :param start_row: int
    :param start_col: int
    :param average: float
    :param width: int
    :param height: int
    :param step: int
    """
    for row in range(start_row, start_row + width):
        for col in range(start_col, start_col + height):
            for i in range(3):
                arr[row][col][i] = int(average // step) * step // 3


def create_grey_pixel_art_from_image(image, width, height, step):
    arr = np.array(image)
    a = len(arr)
    a1 = len(arr[1])
    image_row = 0
    while image_row < a - 1:
        image_col = 0
        while image_col < a1 - 1:
            average = get_area_average(arr, image_row, image_col, width, height)
            change_area_color(arr, image_row, image_col, average, width, height, step)
            image_col = image_col + width
        image_row = image_row + height
    res = Image.fromarray(arr)
    res.save('res.jpg')


def main():
    image_name = input("Введите название изображения для преобразования: ")
    img = Image.open(image_name)
    grey_gradations = int(input("Количество градаций серого: "))
    size = input("Введите размер мозайки в формате 5*5: ")
    cell_size = list(map(int, size.split('*')))
    step = 255 // grey_gradations
    create_grey_pixel_art_from_image(img, cell_size[0], cell_size[1], step)


main()
