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
    for i in range(0, width):
        for j in range(0, height):
            if(i % 2 != 0 or j % 2 != 0):
                matrix[i, j] = (0, 0, 0)


def MirrorVetical(matrix, width, height):
    for i in range(0, int(width / 2)):
        for j in range(0, height):
            r, g, b = matrix[i, j]
            matrix[i, j] = matrix[width - 1 - i, j]
            matrix[width - 1 - i, j] = (r, g, b)


def MirrorHorizontal(matrix, width, height):
    for i in range(0, width):
        for j in range(0, int(height / 2)):
            r, g, b = matrix[i, j]
            matrix[i, j] = matrix[i, height - 1 - j]
            matrix[i, height - 1 - j] = (r, g, b)


def MirrorDiagonal(matrix, width, height):
    for i in range(0, int(width / 2)):
        for j in range(0, height):
            r, g, b = matrix[i, j]
            matrix[i, j] = matrix[width - 1 - i, j]
            matrix[width - 1 - i, j] = (r, g, b)
    for i in range(0, width):
        for j in range(0, int(height / 2)):
            r, g, b = matrix[i, j]
            matrix[i, j] = matrix[i, height - 1 - j]
            matrix[i, height - 1 - j] = (r, g, b)


def MirrorDiagonal2(matrix, width, height):
    MirrorHorizontal(matrix, width, height)
    MirrorVetical(matrix, width, height)


def Negative(matrix, width, height):
    max = 255
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = matrix[i,j]
            matrix[i, j] = (max - r, max - g, max - b)


def Encode(matrix, width, height, message):
    pass


def Decode(original, encoded, width, height):
    pass


image = Image.open("kep.png")
pixelMatrix = image.load()
width, height = image.size
print("Ahoi, this picture's size is: " + str(width) + " x " + str(height))
image.save("modified.png")

