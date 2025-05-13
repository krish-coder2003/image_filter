🎨 Image Filter Web App
This is a simple web app built with Streamlit that allows users to upload an image and apply various filters like Grayscale, Sepia, Blur, Sketch, and Original.

Features
Upload an image: Choose an image in .jpg, .jpeg, or .png format.

Apply filters: Choose from several filters, including:

Original: View the uploaded image without any changes.

Grayscale: Convert the image to grayscale.

Sepia: Apply a warm sepia tone to the image.

Blur: Apply a blur effect to the image.

Sketch: Create a pencil-sketch effect of the image.

Download the filtered image: After applying a filter, download the resulting image.

Requirements
To run this app locally, you need to install the following dependencies:

Python 3.x

Streamlit

OpenCV

Numpy

Pillow

You can install the required dependencies using the following command:

bash
Copy
Edit
pip install -r requirements.txt
Here is the content of the requirements.txt file:

text
Copy
Edit
streamlit
opencv-python
numpy
Pillow
How to Run the App Locally
Clone the repository:

bash
Copy
Edit
git clone https://github.com/kris-coder2003/image-filter-web-app.git
cd image-filter-web-app
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open the app in your browser at http://localhost:8501.

How to Deploy on Streamlit Cloud
To deploy this app on Streamlit Cloud, follow these steps:

Push your repository to GitHub.

Visit Streamlit Cloud.

Click on "New app".

Select the GitHub repository and branch (e.g., main).

Click Deploy and your app will be live.

Project Structure
python
Copy
Edit
image-filter-web-app/
├── app.py          # Main file for Streamlit app
├── filters.py      # Filter logic (applies the image filters)
├── requirements.txt # Dependencies for the project
├── README.md       # Project documentation
└── .gitignore      # Git ignore file
Contributing
Feel free to fork this project, submit issues, or create pull requests if you have any suggestions or improvements.

License
This project is open-source and available under the MIT License.

Enjoy using the Image Filter Web App! 🎨
image-filter-web-app/
├── app.py          # Main file for Streamlit app
├── filters.py      # Filter logic (applies the image filters)
├── requirements.txt # Dependencies for the project
├── README.md       # Project documentation
└── .gitignore      # Git ignore file
Contributing
Feel free to fork this project, submit issues, or create pull requests if you have any suggestions or improvements.
