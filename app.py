import streamlit as st
import numpy as np
from PIL import Image
from filters import apply_filter

# Set up Streamlit app configuration
st.set_page_config(page_title="Image Filter App", layout="centered")
st.title("🎨 Image Filter Web App")
st.markdown("Upload an image and apply a filter of your choice.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Filter options
filter_type = st.selectbox("Choose a filter:", ["Original", "Grayscale", "Sepia", "Blur", "Sketch"])

if uploaded_file is not None:
    # Open the image file using PIL
    image = Image.open(uploaded_file)
    
    # Convert to numpy array (needed for OpenCV operations)
    image_np = np.array(image)

    # Apply the selected filter
    filtered_img = apply_filter(image_np, filter_type)

    # Display result
    st.image(filtered_img, channels="BGR", caption=f"Filtered Image - {filter_type}")

    # Convert back to PIL image for downloading
    result = Image.fromarray(filtered_img)

    # Provide download button
    st.download_button(
        label="📥 Download Image",
        data=result.tobytes(),
        file_name=f"filtered_{filter_type.lower()}.png",
        mime="image/png"
    )
else:
    st.info("Please upload an image to get started.")
