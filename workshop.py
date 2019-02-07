from PIL import Image

image = Image.open("original.png")
pixel_matrix = image.load()
width, height = image.size

for i in range(0, width):
    for j in range(0, height):
        r, g, b = pixel_matrix[i,j]
        pixel_matrix[i,j] = (r + 100, g + 100, b + 100)
        
image.save("light.png")