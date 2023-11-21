import streamlit as st
import base64
from PIL import Image

#from frontend_azoth.config.core import IMAGES_DIR
#from frontend_azoth.utils.gui import create_st_button
from config.core import IMAGES_DIR
from utils.gui import create_st_button

def font_style():
    """
    Set font for the page
    """

    streamlit_style = """
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

                html, body, [class*="css"]  {
                font-family: 'Roboto', sans-serif;
                }
                </style>
                """
    hide_st_style = """
                <style>
                #MainMenu {visibility : hidden;}
                footer {visibility : hidden;}
                header {visibility : hidden;}
                </style>
                """

    st.markdown(streamlit_style, unsafe_allow_html=True)
    st.markdown(hide_st_style, unsafe_allow_html=True)


def header_figure():
    header_container = st.container()
    with header_container:
        st.image(Image.open(str(IMAGES_DIR) + '/AzothAI_logo.png'))


def sidebar_bg(side_bg):

    side_bg_ext = 'png'

    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] > div:first-child {{
            background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html=True,
        )


def sidebar_background():
    """
    Set background image in sidebar
    """
    side_bg = str(IMAGES_DIR) + '/smokes.jpg'
    sidebar_bg(side_bg)


def sidebar_links(links_name, software_link_dict):
    """
    Create page links in sidebar 
    """

    st.sidebar.markdown(links_name)


    if len(software_link_dict) > 1:

        link_1_col, link_2_col, link_3_col = st.sidebar.columns(3)

        i = 0
        link_col_dict = {0: link_1_col, 1: link_2_col, 2: link_3_col}
        for link_text, link_url in software_link_dict.items():

            st_col = link_col_dict[i]
            i += 1
            if i == len(link_col_dict.keys()):
                i = 0

            create_st_button(link_text, link_url, st_col=st_col)

    elif len(software_link_dict) == 1:

        for link_text, link_url in software_link_dict.items():
            create_st_button(link_text, link_url, st_col=st.sidebar)

