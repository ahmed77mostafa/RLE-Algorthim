import cv2
import numpy as np

def rle_encoding(data):
    encoded = []
    prev_value = data[0]
    count = 1

    for value in data[1:]:
        if value == prev_value:
            count += 1
        else:
            encoded.extend([count, prev_value])
            prev_value = value
            count = 1
    encoded.extend([count, prev_value])
    return encoded

def rle_decoding(encoded_data, shape):
    decoded = []

    for i in range(0, len(encoded_data), 2):
        count = encoded_data[i]
        value = encoded_data[i + 1]
        decoded.extend([value] * count)
    return np.array(decoded).reshape(shape)

# 4D2S

gray_image = cv2.imread('434571730_386065660864670_3986189281511690903_n.jpg', cv2.IMREAD_GRAYSCALE)
width = int(gray_image.shape[1] * 0.5)
height = int(gray_image.shape[0] * 0.5)
dim = (width, height)
resized_image = cv2.resize(gray_image, dim, interpolation = cv2.INTER_AREA)

pixels = resized_image.flatten()
compressed_data = rle_encoding(pixels)

decompressed_data = rle_decoding(compressed_data, resized_image.shape)
cv2.imwrite('compressed image.png', decompressed_data)