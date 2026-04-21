import cv2
import pytesseract

# =========================
# SET TESSERACT PATH (Windows)
# =========================
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# =========================
# READ IMAGE
# =========================
img = cv2.imread("download.png")

# Check if image loaded
if img is None:
    print("Image not found")
    exit()

# =========================
# PREPROCESSING
# =========================
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# =========================
# OCR
# =========================
text = pytesseract.image_to_string(thresh)

print("Detected Text:")
print(text)

# =========================
# DISPLAY
# =========================
cv2.imshow("Original", img)
cv2.imshow("Processed", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
