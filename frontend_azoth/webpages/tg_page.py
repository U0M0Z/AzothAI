import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image
import plotly.express as px

#from frontend_azoth.config.core import IMAGES_DIR
#from frontend_azoth.utils.styling import sidebar_background, sidebar_links, font_style

#from frontend_azoth.utils.predict import predict_azothapp

from config.core import IMAGES_DIR, DATASETS_DIR
from utils.styling import sidebar_background, sidebar_links, font_style, header_figure
from utils.predict import predict_azothapp
from utils.smiles_generator import text2smiles

import streamlit as st

def convert_df(df_to_convert):
   return df_to_convert.to_csv(index=False).encode('utf-8')

def tg_page():


#****************************** General streamlit style setup *******************************
    font_style()
    sidebar_background()
    header_figure()

    sns.set_style('darkgrid')
    sns.set(rc={
        'figure.facecolor':(0,0,0,0),
        #'figure.facecolor':'black',
        'axes.labelcolor': 'white',
        'text.color': 'white',
        'xtick.color': 'white',
        'ytick.color': 'white',
        'font.sans-serif': ['Helvetica']
        }
    )

    community_link_dict = {
        "AirUCI": "http://airuci.uci.edu/"
    }
    sidebar_links("## Community-Related Links", community_link_dict)

    database_link_dict = {
        "GitHub Page": "https://github.com/U0M0Z/tgpipe"
    }
    sidebar_links("## Code Source", database_link_dict)

    software_link_dict = {
        "Sklearn": "https://scikit-learn.org/stable/",
        "Streamlit": "https://streamlit.io",
        "XGBoost" : "https://xgboost.ai/",
        "Keras" : "https://keras.io", 
        "Tensorflow" : "https://www.tensorflow.org",
        "RDKit" : "https://www.rdkit.org",
        "mol2vec" : "https://github.com/samoturk/mol2vec"
    }
    sidebar_links("## Software-Related Links", software_link_dict)

#****************************** Page content *******************************
    #logo_container = st.container()
    #logo_container.image(Image.open(str(IMAGES_DIR) + '/logo_tgboost_right_dimensions.jpg'))


    st.title("tg**Boost**")
    st.markdown("---")
    st.markdown(
        """
        This webpage is the Graphical User Interface of tgBoost, a machine learning model to predict glass 
        transition temperature ($T_{\mathrm{g}}$) of organic species considering their molecular structure and functionality for better 
        predictions of the phase state of secondary organic aerosols. tgBoost predicts $T_{\mathrm{g}}$ of monomeric organic \
        molecules from their [SMILES](https://archive.epa.gov/med/med_archive_03/web/html/smiles.html) notations \
        ([Weininger, D. 1988](https://pubs.acs.org/doi/abs/10.1021/ci00057a005)). Here you can interact with tgBoost \
        and make direct predictions on single SMILES, or on your SMILES list by uploading your files. For more details \
        on the base algorithm refer to [Galeazzo and Shiraiwa (2022)](https://pubs.rsc.org/en/content/articlelanding/2022/ea/d1ea00090j).
        """)

    lect_co, mid_co, right_co = st.columns([1, 4, 1])

    img = Image.open(str(IMAGES_DIR) + '/table_of_content_bnw.png')
    mid_co.image(img, output_format="PNG")
    st.markdown(
        """
        Cite as: \n
        Galeazzo, T.; Shiraiwa, M. **Predicting glass transition temperature and melting point of organic compounds \
        via machine learning and molecular embeddings.** Environmental Science: Atmospheres 2022, 2, 362– 374,  DOI: 10.1039/D1EA00090J
        """

    )
    st.markdown("---")
    st.markdown(
        """
        ## Instructions
        """
    )
    st.markdown("---")

    st.markdown(
        """
        #### In the Predict section select either Input: "Single Input" or "File upload" option
        #### 1) Single Input: 
        - Left Box: Enter the canonical SMILES notation of the specie of interest and press "Calculate"
        - Right Box (optional): Search for SMILES notation if needed. If not available please try: \
            [PubChem](https://pubchem.ncbi.nlm.nih.gov/), \
            [National Cancer Institute](https://cactus.nci.nih.gov/chemical/structure). 
        """)

    st.markdown(
        """
        #### 2) File Upload: 
        - Upload a single CSV or Excel file (i.e. *.csv or *.xlsx/xlx extensions) with only a single column with your SMILES compounds. \
            Please name the column "SMILES" and press "Calculate". \n
            EX: 
        """
    )
    lco, mco, rco = st.columns([1, 4, 4])
    df_example = pd.read_csv(str(DATASETS_DIR) + '/SMILES_example.csv')
    lco.table(df_example)
    st.markdown(
        """
        #### 3) File Download: 
        - Download your file by clicking "Download". The dowloaded file containes the input SMILES and their \
            respective $T_{\mathrm{g}}$ as predicted by tgBoost.
        """
    )

    st.markdown("---")

#****************************** Processing and Prediction functions *******************************
    #@st.cache(suppress_st_warning=True)
    def get_df(uploaded_file):

        try:
            file_uploaded_name = uploaded_file.name.split('.')[0]
            file_format = uploaded_file.name.split('.')[1]

            if file_format == 'csv':
                #read csv
                df_uploaded = pd.read_csv(uploaded_file)
            elif file_format == 'xls' or 'xlsx':
                #read csv
                df_uploaded=pd.read_excel(uploaded_file)

            columns_file = df_uploaded.columns

            if 'SMILES' in columns_file:
                pass
            else:
                st.warning('Please rename the SMILES column in your File as "SMILES" and re-upload file')

        except:
            st.warning("You can upload ONLY a csv or excel file")

        return df_uploaded, file_uploaded_name

    #@st.cache()
    def get_predictions(df_to_predict):

        df_wrapped = df_to_predict.copy()

        #url = "http://localhost:8001/api/v1/predict"
        url = 'http://azoth-api.aws-priv.uci.edu/api/v1/predict'
        list_of_smiles = df_wrapped['SMILES'].tolist()

        dict_of_pred = predict_azothapp(url, list_of_smiles)

        if dict_of_pred['errors'] != None: 
            print('Errors: ', len(dict_of_pred['errors']))
        else:
            print('Errors: ', dict_of_pred['errors'])

        smiles_list = dict_of_pred['SMILES']

        df_of_pred = pd.DataFrame(columns = ['SMILES', 'Tg_pred(K)'])
        df_of_pred['SMILES'] = dict_of_pred['SMILES']
        df_of_pred['Tg_pred(K)'] = dict_of_pred['predictions']
        df_of_pred['Tg_pred(K)'] = df_of_pred['Tg_pred(K)'].apply(lambda x: round(float(x), 2))

        return dict_of_pred, df_of_pred


#****************************** File Upload *******************************
    upload_container = st.container()

    with upload_container:

        st.markdown("""## Predict""")
        st.markdown("----")

        opt = st.radio('Input', ['Single Input', 'File Upload'])

        if "compound_name" not in st.session_state:
            st.session_state.compound_name = False
        if "smi_input" not in st.session_state:
            st.session_state.smi_input = False

        if opt == 'Single Input':
            cols = st.columns([3, 1, 3])

            with cols[0]:
                smi_input = st.text_input("Enter Single SMILES👇")
                if smi_input:
                    df1 = pd.DataFrame()
                    df1['SMILES'] = [smi_input.strip()]
                    file_name = smi_input + '_single_SMILES'
                    st.session_state.smi_input = True
                    st.session_state.text_input = True
                    st.session_state.plot = False

            with cols[2]:
                compound_name = st.text_input("Find SMILES - Insert IUPAC name (EX: alpha-pinene)")
                if compound_name:
                    try:
                        smi = text2smiles(compound_name)
                        st.write('Output:', '      ', smi)
                        #st.write(smi)
                        st.session_state.compound_name = True
                    except:
                        st.write('ERROR: check spelling or search online')
                else:
                    st.write(" ")

        else:
            uploaded_file_exp = st.file_uploader("Upload either CSV or Excel files")

            try:
                if uploaded_file_exp is not None:
                    df1, file_name = get_df(uploaded_file_exp)
                    st.session_state.plot = True
                    st.session_state.text_input = False

            except:
                st.warning("[UPLOAD Error]")

#****************************** Calculate *******************************
    st.write(" ")
    calculate_button = st.button("Calculate")

    if calculate_button:
            
        prediction_dict, prediction_df = get_predictions(df1)


        if st.session_state.text_input:

            st.write(prediction_df)

        st.write('tgBoost version: ', prediction_dict['version'])
        st.write('Correct Predictions: ', len(prediction_dict['predictions']), '/', len(prediction_dict['SMILES']))
        st.write('Errors: ', prediction_dict['errors'])

    # Download content
        df_to_csv = convert_df(prediction_df)

        download_button = st.download_button(
            "Press to Download",
            df_to_csv,
            f"tgBoost_predictions_{file_name}.csv",
            "text/csv",
            key='download-csv'
        )

#****************************** Plotting *******************************

        if st.session_state.plot:

            size_prediction_df = len(prediction_df['SMILES'])
            tg_label = ['$T_{\mathrm{g}}$ distribution']

            if size_prediction_df < 100:

                if size_prediction_df < 50:

                    fig = px.histogram(prediction_df, x="Tg_pred(K)", color_discrete_sequence=['limegreen'])
                else:

                    fig = px.histogram(prediction_df, x="Tg_pred(K)", nbins = size_prediction_df/10, color_discrete_sequence=['limegreen'])
            else:

                    fig = px.histogram(prediction_df, x="Tg_pred(K)", nbins = 100, color_discrete_sequence=['limegreen'])

            # Add X and Y labels
            fig.update_xaxes(title_text="<i>T</i><sub>g</sub> (K)")
            fig.update_yaxes(title_text="Count")

            fig.update_layout(
                font = {"family":"Helvetica", "size" : 16},
                width=700, 
                height=700
            )

            st.plotly_chart(fig, theme="streamlit", use_container_width=False)
