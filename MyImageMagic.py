from PIL import Image


def Lighter(matrix, width, height, amount):
    amount = abs(int(amount))
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = matrix[i,j]
            matrix[i, j] = (r + amount, g + amount, g + amount)


def Darker(matrix, width, height, amount):
    amount = abs(int(amount))
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = matrix[i,j]
            matrix[i, j] = (r - amount, g - amount, g - amount)


def BlackAndWhite(matrix, width, height):
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = matrix[i,j]
            average = (r + g + b) / 3
            matrix[i, j] = (int(average), int(average), int(average))


def Mosaic(matrix, width, height):
    pass


def MirrorVetical(matrix, width, height):
    pass


def MirrorHorizontal(matrix, width, height):
    pass


def MirrorDiagonal(matrix, width, height):
    pass


def MirrorDiagonal2(matrix, width, height):
    pass


def Negative(matrix, width, height):
    pass


def Encode(matrix, width, height, message):
    pass


def Decode(original, encoded, width, height):
    pass


image = Image.open("kep.png")
pixelMatrix = image.load()
width, height = image.size
print("Ahoi, this picture's size is: " + str(width) + " x " + str(height))
image.save("modified.png")

