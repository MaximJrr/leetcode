import random


def flipAndInvertImage(image):
    matrix = [[0 for j in range(3)] for i in range(len(image))]
    matrix_pointer, image_pointer = 0, 0

    for i in image:
        for j in i:
            if j == 0:








print(flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))