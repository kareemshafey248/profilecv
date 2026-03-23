import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# Set page configuration
st.set_page_config(
    page_title="Jwira Taha | Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to read text files
def load_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# Function to read binary files and convert to base64
def get_base64_bin(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
            return base64.b64encode(data).decode()
    return ""

# Load assets
html_content = load_file("index.html")
css_content = load_file("style.css")
js_content = load_file("script.js")

# Get Base64 for Image and PDF
profile_b64 = get_base64_bin("profile.jpg")
cv_b64 = get_base64_bin("cv.pdf")

# Inject CSS and JS into HTML
full_html = html_content.replace(
    '<link rel="stylesheet" href="style.css">',
    f'<style>{css_content}</style>'
).replace(
    '<script src="script.js"></script>',
    f'<script>{js_content}</script>'
)

# Inject Profile Image as Base64
if profile_b64:
    full_html = full_html.replace(
        'src="profile.jpg"',
        f'src="data:image/jpeg;base64,{profile_b64}"'
    )

# Inject CV Download as Base64
if cv_b64:
    full_html = full_html.replace(
        'href="cv.pdf"',
        f'href="data:application/pdf;base64,{cv_b64}"'
    )

# Display the portfolio using a custom component
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding: 0;
    }
    footer {display: none;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Render the HTML
# Note: Increasing height for better initial view
components.html(full_html, height=2000, scrolling=True)
