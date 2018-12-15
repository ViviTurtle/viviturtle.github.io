#!/usr/bin/env python

from PIL import Image


#Row One starts on 0,0
START_PIXEL_X = 0
START_PIXEL_Y = 0
# Grid shows 90x90 for each offset
X_NEXT_GRID = 90
Y_NEXT_GRID = 90

# Next pixel to analyzes (if you need to skip pixels chang this)
X_NEXT_pixel = 10
Y_NEXT_pixel = 10

TOTAL_ROWS = 47
TOTAL_COLUMNS = 152


class ancient_letter(object):

    def __init__(self, image_reader, x_start: int, y_start: int):
        """
        :param image_path: The image reader
        :param x: The starting x coordinate of the grid
        :param y: The starting y coordinate of the grid
        """
        im = image_reader  # Can be many different formats.
        pix = im.load()
        rgb_im = im.convert('RGB')
        self.pixel_strings = ''
        #print(f'----- X Start = {x_coo}, Y Start = {y_coo}-----')
        for x in range(x_start, x_start+X_NEXT_GRID, X_NEXT_pixel):
            for y in range(y_start, y_start+Y_NEXT_GRID,Y_NEXT_pixel):
               # print(f'X Pixel = {x}, Y Pixel = {y}')
                r, g, b = rgb_im.getpixel((x,y))
                #print(f'The red, blue, and green values are {r},{g},{b}')
                if r > 200 and g > 200 and b > 200:
                    self.pixel_strings += "0"
                else:
                    self.pixel_strings += "1"
                #print(f"The pixel string is {self.pixel_strings}")
        #print(f"The hash of this is {self.__hash__()}")

    def __eq__(self, other):
        if self.__hash__() == other.__hash__():
            return True

    def __hash__(self):
        """Returns Integer of Binary Data Spixel Strings"""
        return int(self.pixel_strings, 2)

    def __repr__(self):
        return str(self.__hash__())


def grid_to_text(image_path):
    """"""
    alphabet = {0: " "}
    wishlist = ""
    current_ascii_letter = 97
    im = Image.open(image_path)  # Can be many different formats.
    pix = im.load()
    for y in range(1, TOTAL_COLUMNS, 2):
        for x in range(TOTAL_ROWS):


            #print(f'----- X coor = {x}, Y coor = {y}-----')
            current_letter = ancient_letter(im, x * X_NEXT_GRID, y * Y_NEXT_GRID)
            if current_letter not in alphabet:
                alphabet[current_letter] = str(chr(current_ascii_letter))
                current_ascii_letter += 1
            wishlist += alphabet[current_letter]
           # print(f'The current alphabet is: {alphabet}')
            print(f'The current text is: {wishlist}')
    print(wishlist)


grid_to_text("/Users/vivi.langga/Downloads/wishlist.png")
