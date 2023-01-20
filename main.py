# Import the necessary libraries
import time
import cv2
import pyautogui
import numpy as np
import turtle
#by Bruman3

#setting up turtle window, pen, etc
twindow = turtle.Screen()
twindow.bgcolor("black")
#You can edit window size
twindow.setup(700,700)
bb = turtle.Turtle()
pen = bb.getpen()
pen.hideturtle()
#play with coords to findn preferable location
pen.goto(-290,-270)
pen.color("white")
turtle.pendown()
turtle.tracer(0)

# create function to image ---> ascii
def to_ascii(image):
    # create an empty string to store the ASCII art
    ascii_art = ""
    
    #change dsize to change to quality of the output, makes the input smaller so less assci char are used
    #scale up/down numbers for dsize            [desize(width, height)]
    image = cv2.resize(image, dsize=(230, 60))
    
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Iterate over each pixel in the image
    for y in range(height):
        for x in range(width):
            # get pixel value
            pixel = image[y][x]
            # Convert the pixel value to its grayscale equivalent
            grayscale = sum(pixel) / len(pixel)
            # Convert the grayscale value to its ASCII equivalent
            ascii_char = chr(int(grayscale / 255 * 94) + 33)
            # add the ASCII character to the ASCII art string
            ascii_art += ascii_char
        ascii_art += "\n"
    return ascii_art

#customize font size, type, etc
FONTSIZE = 4
FONT = ('Arial', FONTSIZE, 'normal')

# Get the next frame from the camera
while True:
    #change region location to change area on screen and size
    img = pyautogui.screenshot( region=(231,188,907,673))
    frame = np.array(img)
    #calls funtion
    ascii_art = to_ascii(frame)
    #prints a text with turtle pen on a turtle window
    pen.write(ascii_art, font = FONT)
    time.sleep(0.5)
    pen.clear()
