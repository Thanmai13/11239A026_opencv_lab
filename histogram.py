import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Histogram for grayscale
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Number of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
