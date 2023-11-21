import streamlit as st
from PIL import Image

from config.core import IMAGES_DIR

from utils.styling import font_style, sidebar_background

def contact_page():

    font_style()

    sidebar_background()

    st.title("Contact")

    cols = st.columns(2)

    with cols[0]:

        img1 = Image.open(str(IMAGES_DIR) + '/shiraiwa_contact.png')
        new_img1 = img1.resize((200, 200))
        st.image(new_img1, output_format="PNG")

    
    with cols[1]:

        img2 = Image.open(str(IMAGES_DIR) + '/galeazzo_contact.png')
        new_img2 = img2.resize((200, 200))
        st.image(new_img2, output_format="PNG")

