import streamlit as st
from streamlit_option_menu import option_menu

from PIL import Image

#from frontend_azoth.webpages.home_page import home_page
#from frontend_azoth.webpages.about_page import about_page
#from frontend_azoth.webpages.tg_page import tg_page
#from frontend_azoth.webpages.vp_page import vp_page
from webpages.home_page import home_page
from webpages.about_page import about_page
from webpages.contact_page import contact_page
from webpages.tg_page import tg_page
from webpages.vp_page import vp_page

#from frontend_azoth.utils.styling import font_style

#from frontend_azoth.config.core import IMAGES_DIR

from utils.styling import font_style

from config.core import IMAGES_DIR


class MultiApp:
    def __init__(self):
        self.apps = []
        self.app_func = {}

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})
        self.app_func[title] = func

    def run(self):

        img = Image.open(str(IMAGES_DIR) +'/airai_logo_small.png')
        st.set_page_config(page_title="AzothAI", page_icon=img, layout="wide")

        MENU_OPTIONS = ["Home", "About", "Models"]

        with st.sidebar:
            st.markdown("#")
            menu_action = option_menu("Main Menu", MENU_OPTIONS, 
                icons=['house', 'bookmark-star-fill', 'play'], menu_icon="cast", default_index=0)

        menu_id = MENU_OPTIONS.index(menu_action)

        st.sidebar.markdown("### Contact: tgaleazz@uci.edu")

        if menu_id == 0:
            home_page()
        elif menu_id == 1:
            about_page()
        elif menu_id == 2:
            st.sidebar.markdown("## Models Menu")
            app = st.sidebar.selectbox("Select Model", self.apps, format_func=lambda app: app["title"])
            st.sidebar.markdown("---")
            self.app_func[app["title"]]()
            #app["function"]()

app = MultiApp()

app.add_app("tgBoost", tg_page)
app.add_app("Coming Soon", vp_page)

app.run()