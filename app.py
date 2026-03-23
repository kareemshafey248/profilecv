import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configuration
st.set_page_config(
    page_title="Jwira Taha | Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to read files
def load_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# Load assets
html_content = load_file("index.html")
css_content = load_file("style.css")
js_content = load_file("script.js")

# Inject CSS and JS into HTML
# We remove the external links to style.css and script.js and embed them directly
full_html = html_content.replace(
    '<link rel="stylesheet" href="style.css">',
    f'<style>{css_content}</style>'
).replace(
    '<script src="script.js"></script>',
    f'<script>{js_content}</script>'
)

# Display the portfolio using a custom component to allow full height
# We use a container that takes up the full width/height
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
components.html(full_html, height=1200, scrolling=True)
