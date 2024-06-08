# ============================================================================= #
# This program attempts to hide a message in an image. The message is hidden by #
# modifying the colour values some of the pixels in a given image.              #
# ============================================================================= #

from PIL import Image
from typing import List

# gives a new value for x such that x % base = y
def adjust_value_for_base(x: int, base: int, y: int, limit=255) -> int:
    # calculate the current remainder of x modulo base
    current_remainder = x % base

    # calculate the difference needed to reach the desired remainder y
    difference = current_remainder - y

    # adjust x by subtracting the difference
    adjusted_x = x - difference

    # if the adjusted value exceeds the limit, adjust within range
    if adjusted_x > limit:
        adjusted_x -= base
    elif adjusted_x < 0:
        adjusted_x += base

    # Ensure the final value is within the limit and satisfies the condition
    if adjusted_x > limit:
        raise ValueError("Cannot adjust value to meet requirements within the given constraints.")
    
    return adjusted_x

def string_to_alphabet_index(text: str) -> int:
    # convert the text to lowercase
    text = text.upper()
    # convert the text to an integer by converting each character to its
    # corresponding index in the alphabet
    return [ord(char) - ord('A') for char in text]

def alphabet_index_to_string(indexes: List[int]) -> str:
    # convert the indexes to a string by converting each index to its
    # corresponding character in the alphabet
    return ''.join([chr(index + ord('A')) for index in indexes])

# how encryption works:
# we modifty one of the colour values in each offset'th pixel
# such that that value modulo base is equal to the corresponding
# letter of the alphabet example:
# text = "c" (= 2)
# rgb of the target pixel = (255, 40, 39)
# base = 17
# colour_to_modify = 1 (blue)
# so pixel.blue % 17 = 2, use adjust_value_for_base to find the
# new value for pixel.blue
def encrypt(
        text: str, # key to encrypt
        image_path: str, # path to the image file
        colour_to_modify: int, # r = 0, g = 1, b = 2
        offset: int, # each offset's pixel will be affected
        base: int, # must be greater than 26, so that all letters of the alphabet can be represented
        ) -> None:
    # validate the base is large enough
    if base < 26:
        raise ValueError("Base must be at least 26")
    
    # read the image file
    image = Image.open(image_path)

    # get the width and height of the image
    width, height = image.size

    # check that the offset, text lenght and image width are compatible
    if (width * height) / offset < len(text):
        raise ValueError("The image is too small to hide the message")
    
    # get the pixel data from the image
    pixels = image.load()

    # convert the text to a list of alphabet indexes
    indexes = string_to_alphabet_index(text)

    # iterate over the indexes and modify the corresponding pixel
    for i, alphabet_index in enumerate(indexes):
        # calculate the pixel position
        x = i * offset % width
        y = i * offset // width

        # get the pixel
        pixel = list(pixels[x, y])

        # adjust the colour value
        pixel[colour_to_modify] = adjust_value_for_base(pixel[colour_to_modify], base, alphabet_index)

        # save the modified pixel
        pixels[x, y] = tuple(pixel)

    # save the modified image
    image.save(f'encrypted_{image_path}')

def decrypt(
        image_path: str, # path to the image file
        colour_modified: int, # r = 0, g = 1, b = 2
        offset: int, # each offset's pixel will be affected
        base: int, # must be greater than 26, so that all letters of the alphabet can be represented
        ) -> str:
    # validate the base is large enough
    if base < 26:
        raise ValueError("Base must be at least 26")
    
    # read the image file
    image = Image.open(image_path)

    # get the width and height of the image
    width, height = image.size

    # get the pixel data from the image
    pixels = image.load()

    # create a list to store the alphabet indexes
    indexes = []

    # iterate over the pixels and extract the modified colour value
    for i in range((width * height) // offset):
        # calculate the pixel position
        x = i * offset % width
        y = i * offset // width

        # get the pixel
        pixel = list(pixels[x, y])

        # calculate the alphabet index
        alphabet_index = pixel[colour_modified] % base

        # add the alphabet index to the list
        indexes.append(alphabet_index)

    # convert the alphabet indexes to a string
    return alphabet_index_to_string(indexes)