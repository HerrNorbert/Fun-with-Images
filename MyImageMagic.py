from PIL import Image

def lighter(matrix, width, height, amount):
    amount = abs(int(amount))
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = matrix[i, j]
            matrix[i, j] = (r + amount, g + amount, b + amount)

def darker(matrix, width, height, amount):
    amount = abs(int(amount))
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = matrix[i, j]
            matrix[i, j] = (r - amount, g - amount, b - amount)

def black_and_white(matrix, width, height):
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = matrix[i,j]
            average = (r + g + b) / 3
            matrix[i, j] = (int(average), int(average), int(average))

def mosaic(matrix, width, height):
    for i in range(0, width):
        for j in range(0, height):
            if(i % 2 != 0 or j % 2 != 0):
                matrix[i, j] = (0, 0, 0)

def mirror_vetical(matrix, width, height):
    for i in range(0, int(width / 2)):
        for j in range(0, height):
            r, g, b = matrix[i, j]
            matrix[i, j] = matrix[width - 1 - i, j]
            matrix[width - 1 - i, j] = (r, g, b)

def mirror_horizontal(matrix, width, height):
    for i in range(0, width):
        for j in range(0, int(height / 2)):
            r, g, b = matrix[i, j]
            matrix[i, j] = matrix[i, height - 1 - j]
            matrix[i, height - 1 - j] = (r, g, b)

def mirror_diagonal(matrix, width, height):
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

def mirror_diagonal_2(matrix, width, height):
    mirror_horizontal(matrix, width, height)
    mirror_vetical(matrix, width, height)

def negative(matrix, width, height):
    max = 255
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = matrix[i,j]
            matrix[i, j] = (max - r, max - g, max - b)

def Encode(matrix, width, height, message):
    charIndex = 0
    charOffSet = ord('A')
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = matrix[i, j]
            charCode = ord(message[charIndex])
            encodedChar = charCode - charOffSet
            integrate = int(encodedChar / 3)
            leftOver = encodedChar - (integrate * 3)
            checkSum = integrate + leftOver
            matrix[i, j] = (r + integrate, g + leftOver, b + checkSum)
            if len(message) > charIndex + 1:
                charIndex += 1
            else:
                return

def Decode(original, encoded, width, height):
    message = ""
    charOffSet = ord('A')
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = encoded[i, j]
            oR, oG, oB = original[i, j]
            r -= oR
            g -= oG
            b -= oB
            if r + g == b and r != 0:
                message += chr(charOffSet + 3 * r + g)
            elif r + g != b :
                message += '☠️'
            else:
                return message

image = Image.open("kep.png")
pixelMatrix = image.load()
width, height = image.size
print("Ahoi, this picture's size is: " + str(width) + " x " + str(height))
image.save("modified.png")
