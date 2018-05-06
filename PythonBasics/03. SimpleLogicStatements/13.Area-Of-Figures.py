import math

figureType = input()

area = None

if figureType == "square" or figureType == "circle":
    size = float(input())

    if figureType == "square":
        area = size * size
    else:
        area = math.pi * size * size
elif figureType == "rectangle" or figureType == "triangle":
    size1 = float(input())
    size2 = float(input())

    if figureType == "rectangle":
        area = size1 * size2
    else:
        area = size1 * size2 / 2

if area != None:
    print("{0:.3f}".format(area))
