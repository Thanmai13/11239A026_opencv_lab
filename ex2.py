import cv2
img = cv2.imread("image.jpg")
# Image properties
height, width, channels = img.shape
size = img.size
datatype = img.dtype
print("Width :", width)
print("Height :", height)
print("Channels :", channels)
print("Image Size :", size)
print("Data Type :", datatype)
