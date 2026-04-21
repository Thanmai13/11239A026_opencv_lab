import cv2
import pytesseract
import numpy as np
from tkinter import Tk, filedialog

# =========================
# SET TESSERACT PATH (IMPORTANT)
# =========================
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# =========================
# FILE PICKER
# =========================
def select_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    return file_path

# =========================
# LOAD IMAGE
# =========================
image_path = select_image()

if not image_path:
    print("No file selected")
    exit()

print("Loaded File:", image_path)

image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to load image")
    exit()

orig = image.copy()

# =========================
# PREPROCESSING
# =========================
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Remove noise
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Dilation to group text
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilate = cv2.dilate(thresh, kernel, iterations=1)

# =========================
# TEXT DETECTION
# =========================
contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours (top to bottom)
contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[1])

print("\nDetected Text:\n")

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Filter small noise
    if w > 50 and h > 30:
        roi = orig[y:y+h, x:x+w]

        # 🔥 Avoid empty ROI error
        if roi is None or roi.size == 0:
            continue

        # OCR config
        config = '--oem 3 --psm 6 -l eng'

        text = pytesseract.image_to_string(roi, config=config)

        if text.strip():
            print(text.strip())

            # Draw rectangle
            cv2.rectangle(orig, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Put detected text
            cv2.putText(orig, text.strip(), (x, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 1)

# =========================
# OUTPUT
# =========================
cv2.imshow("Text Detection + Recognition", orig)
cv2.waitKey(0)
cv2.destroyAllWindows()