import cv2
import numpy as np

def rle_encoding(data):
    encoded_string = ''
    prev_char = ''
    count = 1
    for char in data:
        if char != prev_char:
            if prev_char:
                encoded_string += str(count) + prev_char
            prev_char = char
            count = 1
        else:
            count += 1
    encoded_string += str(count) + prev_char
    return encoded_string

def rle_decoding(data):
    decoded_string = ''
    count = ''

    for char in data:
        if char.isdigit():
            count += char
        else:
            decoded_string += char * int(count)
            count = ''
    return decoded_string

string = input()
decoded_string = rle_decoding(string)
print(decoded_string)
