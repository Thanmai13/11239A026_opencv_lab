import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

colors = ('b', 'g', 'r')

plt.title("Color Histogram")

for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)

plt.xlim([0, 256])
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()
