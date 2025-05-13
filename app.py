import streamlit as st
import cv2
import numpy as np
from PIL import Image
from filters import apply_filter

st.set_page_config(page_title="Image Filter App", layout="centered")
st.title("🎨 Image Filter Web App")
st.markdown("Upload an image and apply a filter of your choice.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Filter options
filter_type = st.selectbox("Choose a filter:", ["Original", "Grayscale", "Sepia", "Blur", "Sketch"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Apply filter
    filtered_img = apply_filter(image_np, filter_type)

    # Display result
    st.image(filtered_img, channels="BGR", caption=f"Filtered Image - {filter_type}")

    # Convert to download-friendly format
    result = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)
    result_pil = Image.fromarray(result)

    # Download button
    st.download_button(
        label="📥 Download Image",
        data=result_pil.tobytes(),
        file_name=f"filtered_{filter_type.lower()}.png",
        mime="image/png"
    )
else:
    st.info("Please upload an image to get started.")
