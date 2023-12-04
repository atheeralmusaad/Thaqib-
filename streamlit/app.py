# Python In-built packages
from pathlib import Path


# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="ثاقب | Thaqib",
    page_icon="👜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("X-ray Baggage Scanner Detection")
image = "logo.png"
st.sidebar.image(image, width=400)



# Model Options


confidence = float(25) / 100

# Selecting Detection Or Segmentation

model_path = Path(settings.DETECTION_MODEL)


# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

# st.sidebar.header("Image/Video Config")
source_radio = 'Video'

source_img = None

helper.play_stored_video(confidence, model)
