#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import random
#defining class for encyrpting image
def encrypting_image(image_path, output_path):
    image = Image.open("C:\\Users\\arfat\\Downloads\\parrot.jpg")
    pixels = image.load("C:\\Users\\arfat\\Downloads\\parrot.jpg")
    #Specifying the height and width of image
    width, height = image.size
    for x in range(width):
        for y in range(height):
          # Randomly swap pixel values
                random_x, random_y = random.randint(0, width - 1), random.randint(0, height - 1)
                pixels[x, y], pixels[random_x, random_y] = pixels[random_x, random_y], pixels[x, y]
                image.save("C:\\Cyber\\encyrpted_image.jpg") # Using output_path parameter and save within the function
                return output_path
                # Calling the Function with correct arguements
                encrypting_image("C:\\Users\\arfat\\Downloads\\parrot.jpg", "C:\\Cyber\\encrypted_image.jpg")
                image_path = "input_image.jpg"
                encrypted_path = "encrypted_image.jpg"
                encrypting_image(image_path="C:\\Users\\arfat\\Downloads\\parrot.jpg", output_path="C:\\Cyber\\encyrpted_image.jpg")
#defining class for decrypting image
def decrypting_image(image_path, output_path):
    image = Image.open("C:\\Users\\arfat\\Downloads\\parrot.jpg")
    pixels = image.load("C:\\Users\\arfat\\Downloads\\parrot.jpg")
    #Specifying the height and width of image
    width, height = image.size
    for x in range(width):
        for y in range(height):
          # Randomly swap pixel values
                random_x, random_y = random.randint(0, width - 1), random.randint(0, height - 1)
                pixels[x, y], pixels[random_x, random_y] = pixels[random_x, random_y], pixels[x, y]
                image.save("C:\\Cyber\\decyrpted_image.jpg") # Using output_path parameter and save within the function
                return output_path
                # Calling the Function with correct arguements
                decrypting_image("C:\\Users\\arfat\\Downloads\\parrot.jpg", "C:\\Cyber\\decrypted_image.jpg")
                image_path = "input_image.jpg"
                decrypted_path = "decrypted_image.jpg"
                decrypting_image(image_path="C:\\Users\\arfat\\Downloads\\parrot.jpg", output_path="C:\\Cyber\\decyrpted_image.jpg")
                encrypt_image("input_image.jpg","encrypted_image.jpg")
                decrypt_image("encrypted_image.jpg","decrypted_image.jpg")
