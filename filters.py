import cv2
import numpy as np

def apply_filter(image, filter_type):
    if filter_type == "Original":
        # Return the image unchanged for the "Original" filter
        return image
    
    elif filter_type == "Grayscale":
        # Convert the image to grayscale
        return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    elif filter_type == "Sepia":
        # Apply the sepia filter
        image = image.astype(np.uint8)
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])

        sepia_image = cv2.transform(image, kernel)
        return np.clip(sepia_image, 0, 255).astype(np.uint8)
    
    elif filter_type == "Blur":
        # Apply a blur filter
        return cv2.GaussianBlur(image, (15, 15), 0)
    
    elif filter_type == "Sketch":
        # Apply the sketch effect
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        inv = 255 - gray
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        sketch = cv2.divide(gray, 255 - blur, scale=256.0)
        return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    
    else:
        # Return the original image if the filter type is not recognized
        return image
