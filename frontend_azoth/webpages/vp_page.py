import streamlit as st
from PIL import Image

#from frontend_azoth.utils.gui import create_st_button
#from frontend_azoth.config.core import IMAGES_DIR

#from frontend_azoth.utils.styling import font_style, sidebar_background, sidebar_links

from utils.gui import create_st_button
from config.core import IMAGES_DIR

from utils.styling import font_style, sidebar_background, sidebar_links

def vp_page():

    font_style()

    software_link_dict = {
        "Streamlit": "https://streamlit.io",
        "DGL" : "https://www.dgl.ai/",
        "Keras" : "https://keras.io", 
        "PyTorch" : "https://pytorch.org/",
        "RDKit" : "https://www.rdkit.org",
        "DeepChem" : "https://github.com/deepchem"
    }

    sidebar_background()
    sidebar_links("## Software-Related Links", software_link_dict)

    st.title("Coming Soon")

    cs_left, cs_mid, cs_right = st.columns([1,1,1])

    cs_left.image(Image.open(str(IMAGES_DIR) + '/dalle1.jpg'))
    cs_mid.image(Image.open(str(IMAGES_DIR) + '/dalle2.jpg'))
    cs_right.image(Image.open(str(IMAGES_DIR) + '/dalle3.jpg'))

    st.markdown(
        """
        © Tommaso Galeazzo
        """
        )