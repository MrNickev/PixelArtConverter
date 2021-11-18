from PIL import Image
import numpy as np


    average = 0
    for row in range(startRow, startRow + cell_size[0]):
        for col in range(startCol, startCol + cell_size[1]):
            n1 = int(arr[row][col][0])
            n2 = int(arr[row][col][1])
            n3 = int(arr[row][col][2])
            M = n1 + n2 + n3
            average += M
    average = int(average // (cell_size[0] * cell_size[1]))
    return average


def changeAreaColor(arr, startRow, staartCol, average):
    for row in range(startRow, startRow + cell_size[0]):
        for col in range(staartCol, staartCol + cell_size[1]):
            arr[row][col][0] = int(average // step) * step // 3
            arr[row][col][1] = int(average // step) * step // 3
            arr[row][col][2] = int(average // step) * step // 3


def createGreyPixelArtFromImage():
    arr = np.array(img)
    a = len(arr)
    a1 = len(arr[1])
    image_row = 0
    while image_row < a - 1:
        image_col = 0
        while image_col < a1 - 1:
            average = getAreaAverage(arr, image_row, image_col)
            changeAreaColor(arr, image_row, image_col, average)
            image_col = image_col + cell_size[0]
        image_row = image_row + cell_size[1]
    res = Image.fromarray(arr)
    res.save('res.jpg')


img = Image.open("img2.jpg")
grey_gradations = 5
cell_size = [5, 5]
step = 255 // grey_gradations

# arr = np.array(img)
# a = len(arr)
# a1 = len(arr[1])
# image_row = 0
# while image_row < a - 1:
#     image_col = 0
#     while image_col < a1 - 1:
#         s = getAreaAverage()
#         changeAreaColor()
#         image_col = image_col + cell_size[0]
#     image_row = image_row + cell_size[1]
# res = Image.fromarray(arr)
# res.save('res.jpg')
