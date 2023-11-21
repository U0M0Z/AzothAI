import streamlit as st

from PIL import Image

#from frontend_azoth.config.core import IMAGES_DIR
#from frontend_azoth.utils.styling import sidebar_background, sidebar_links, font_style
from config.core import IMAGES_DIR
from utils.styling import sidebar_background, sidebar_links, font_style, header_figure

def about_page():
    
    font_style()
    sidebar_background()
    header_figure()

    community_link_dict = {
        "AirUCI": "http://airuci.uci.edu/"
    }
    sidebar_links("## Community-Related Links", community_link_dict)


    header_container = st.container()
    header_container.markdown("## About")
    header_container.markdown("---")

    header_container.markdown(
            """
            In recent years artificial intelligence (AI) techniques have helped building new scientific knowledge and tools from data. \
            This trend suggests that AI applications are emerging as the fourth pillar of science together with experimentation, \
            theory and computation
            ([O. Anatole von Lilienfeld, 2020](https://iopscience.iop.org/article/10.1088/2632-2153/ab6d5d)). 

            AzothAI is a project created by Dr. Tommaso Galeazzo and Prof. Manabu Shiraiwa and \
            hosted by the University of California, Irvine. Its purpose is to gather the AI models developed in \
            the [Shiraiwa Group](https://sites.uci.edu/shiraiwalab/) at the University of California, Irvine. \
            Among the others, the core models developed include tgBoost, a Machine Learning (ML) powered model based on an \
            Extreme Gradient Boosting method (XGBoost) and molecular embeddings (mol2vec). \n
            #
            #
            #
            ##### For any questions or inquiries please contact:
            Dr. Tommaso Galeazzo        tgaleazz@uci.edu \n
            Prof. Manabu Shiraiwa       m.shiraiwa@uci.edu

            """
        )

    header_container.markdown(

        """
        #
        #
        #
        """
    )

    logo_cols = st.columns([1,9])

    with logo_cols[0]:
        stemma = Image.open(str(IMAGES_DIR) + '/uci_white_logo.png')
        new_image = stemma.resize((75, 75))
        st.image(new_image)

    with logo_cols[1]:
        logo = Image.open(str(IMAGES_DIR) + '/uci_department_of_chemsitry.png')
        new_logo = logo.resize((500, 75))
        st.image(new_logo)
