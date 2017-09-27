from PIL import Image


def Lighter(matrix, width, height, amount):
    pass


def Darker(matrix, width, height, amount):
    pass


def BlackAndWhite(matrix, width, height):
    pass


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


image = Image.open("encoded.png")
pixelMatrix = image.load()
width, height = image.size
print("Ahoi, this picture's size is: " + str(width) + " x " + str(height))
