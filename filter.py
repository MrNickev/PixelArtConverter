from PIL import Image
import numpy as np


def getAreaAverage(arr, startRow, startCol, width, height):
    """
    Return average value of area. Sizes of area are in cell_size

    :param arr: array
    :param startRow: int
    :param startCol: int
    :param width: int
    :param height: int
    :return: float

    >>> getAreaAverage([[[100, 100, 100], [200, 200, 200]], [[200, 200, 200], [100, 100, 100]]], 0, 0, 2, 2)
    450
    """
    average = 0
    for row in range(startRow, startRow + height):
        for col in range(startCol, startCol + height):
            n1 = int(arr[row][col][0])
            n2 = int(arr[row][col][1])
            n3 = int(arr[row][col][2])
            M = n1 + n2 + n3
            average += M
    average = int(average // (width * height))
    return average


def changeAreaColor(arr, startRow, staartCol, average, width, height, step):
    """
    Change pixels for average in area
    :param arr: array
    :param startRow: int
    :param staartCol: int
    :param average: float
    :param width: int
    :param height: int
    :param step: int
    """
    for row in range(startRow, startRow + width):
        for col in range(staartCol, staartCol + height):
            arr[row][col][0] = int(average // step) * step // 3
            arr[row][col][1] = int(average // step) * step // 3
            arr[row][col][2] = int(average // step) * step // 3


def createGreyPixelArtFromImage(image, width, height, step):
    arr = np.array(image)
    a = len(arr)
    a1 = len(arr[1])
    image_row = 0
    while image_row < a - 1:
        image_col = 0
        while image_col < a1 - 1:
            average = getAreaAverage(arr, image_row, image_col, width, height)
            changeAreaColor(arr, image_row, image_col, average, width, height, step)
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
    createGreyPixelArtFromImage(img, cell_size[0], cell_size[1], step)

main()
