import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

# Different smoothing methods
avg_blur = cv2.blur(img, (7, 7))
gaussian_blur = cv2.GaussianBlur(img, (7, 7), 0)
median_blur = cv2.medianBlur(img, 7)
bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Original", img)
cv2.imshow("Average Blur", avg_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Bilateral Filter", bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
