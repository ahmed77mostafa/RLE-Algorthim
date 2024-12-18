import cv2
import numpy as np

def rle_encoding(data):
    encoding = []
    prev_value = data[0]
    count = 1

    for value in data[1:]:
        if value == prev_value:
            count += 1
        else:
            encoding.extend([prev_value, count])
            prev_value = value
            count = 1  # Reset count to 1 for the new value
    encoding.extend([prev_value, count])  # Append the last value and count
    return encoding

def rle_decoding(encoded_data, shape):
    decoded_data = []
    for i in range(0, len(encoded_data), 2):
        value = encoded_data[i]
        count = encoded_data[i + 1]
        decoded_data.extend([value] * count)
    return np.array(decoded_data).reshape(shape)

# Load the grayscale image
gray_image = cv2.imread('332961565_1102563874471718_8746248417768347334_n.jpg', cv2.IMREAD_GRAYSCALE)
if gray_image is None:
    raise ValueError("Image not found or unable to load.")

# Resize the image to half its original dimensions
width, height = int(gray_image.shape[1] * 0.5), int(gray_image.shape[0] * 0.5)
dim = (width, height)
gray_image = cv2.resize(gray_image, dim)

# Flatten the image pixels for RLE encoding
pixels = gray_image.flatten()

# Apply RLE encoding
compressed_data = rle_encoding(pixels)

# Ensure that compressed_data can fit into uint8
if any(value > 255 for value in compressed_data):
    raise ValueError("Compressed values exceed 255, cannot be stored in uint8.")

# Create a NumPy array for the compressed data
compressed_array = np.array(compressed_data, dtype=np.uint8)

# Save the compressed data to a .npy file
np.save('compressed_image.npy', compressed_array)

# Decompress the data to reconstruct the image
decompressed_data = rle_decoding(compressed_data, gray_image.shape)

# Save the decompressed image as a .bmp file
desktop_path = "compressed.bmp"
cv2.imwrite(desktop_path, decompressed_data)

print("Compression complete. Decompressed image saved as 'compressed.bmp'.")