import streamlit as st

from PIL import Image

#from frontend_azoth.config.core import IMAGES_DIR
#from frontend_azoth.utils.styling import sidebar_background, sidebar_links, font_style
from config.core import IMAGES_DIR
from utils.styling import sidebar_background, sidebar_links, font_style, header_figure

def home_page():

    font_style()
    sidebar_background()
    header_figure()

    community_link_dict = {
        "AirUCI": "http://airuci.uci.edu/"
    }
    sidebar_links("## Community-Related Links", community_link_dict)



    header_container = st.container()

    header_container.markdown("## A platform for AI powered tools for prediction of physical properties of organic molecules")

    body_container = st.container()
    body_container.markdown("---")

    body_container.markdown(
        """
        ### Welcome 👋 👋 👋
        **AzothAI** is a platform to host Artificial Intelligence (AI) models for physical and \
        atmospheric chemistry. \n
        
        Researchers can use AzothAI and its models to gain novel insights into aerosol modeling \
        and its applications to climate and air quality models.
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        ### Usage
        On the left sidebar select **“Models”** and the desired model from the drop down **“Models Menu”**. 
        """
    )
    st.markdown("---")