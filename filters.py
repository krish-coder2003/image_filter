import cv2
import numpy as np

def apply_filter(image, filter_type):
    if filter_type == "Original":
        return image
    elif filter_type == "Grayscale":
        return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    elif filter_type == "Sepia":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia = cv2.transform(image, kernel)
        return np.clip(sepia, 0, 255).astype(np.uint8)
    elif filter_type == "Blur":
        return cv2.GaussianBlur(image, (15, 15), 0)
    elif filter_type == "Sketch":
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        inv = 255 - gray
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        sketch = cv2.divide(gray, 255 - blur, scale=256.0)
        return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    else:
        return image
