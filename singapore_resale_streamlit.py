import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pickle

st.set_page_config(
    page_title="Singapore Resale Flat Price Predicting",
    page_icon="🏨",
    layout="wide")




with st.sidebar:
    selected = option_menu("Main Menu", ["About Project", "Resale Price Prediction"],
                           icons=["house", "gear"],
                           styles={"nav-link": {"font": "sans serif", "font-size": "20px", "text-align": "centre"},
                                   "nav-link-selected": {"font": "sans serif", "background-color": "#fc0303"},
                                   "icon": {"font-size": "20px"}
                                   }
                           )
    



if selected == "About Project":
    st.markdown("# :red[Singapore Resale Flat Price Predicting]")
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
    st.markdown("### :red[Technologies :] Python, Pandas, Numpy, Scikit-Learn, Streamlit, Python scripting, "
                "Machine Learning, Data Preprocessing, Visualization, EDA, Model Building, Data Wrangling, "
                "Model Deployment")
    st.markdown("### :red[Overview :] This project aims to construct a machine learning model and implement "
                "it as a user-friendly online application in order to provide accurate predictions about the "
                "Reselling price of the flat in Singapore. This prediction model will be based on past data.")   




if selected == "Resale Price Prediction":
    st.markdown("# :red[Predicting Results based on Trained Model]")
    col1,col2 = st.columns(2)
    with col1:
        a1 = st.text_input("Town")
        b1 = st.text_input("Flat_type")
        c1 = st.text_input("Storey_range")
        d1 = st.text_input("Floor_SQM")
        e1 = st.text_input("Flat_Model")
        f1 = st.text_input("Year")
        g1 = st.text_input("Month")
        h1 = st.text_input("Remaining Lease Year")
        i1 = st.text_input("Remaining Lease Month")
        j1 = st.text_input("Lease_Commence_Year")

            
    with open(r"F:\DS\MDTM20\VS Code\Singapore\resale_final_model.pkl", 'rb') as file_1:
        regression_model = pickle.load(file_1)

    with col2:  
        predict_button_1 = st.button("Predict Resale Price", type = "primary")

        if predict_button_1:

            a1 = int(a1)
            b1 = int(b1)
            c1 = int(c1)
            d1 = float(d1)
            e1 = int(e1)
            f1 = float(f1)
            g1 = int(g1)
            h1 = float(h1)
            i1 = float(i1)
            j1 = int(j1)


            # -----Sending the user enter values for prediction to our model-----
            new_sample_1 = np.array(
                    [[a1, b1, c1, d1, e1, f1, g1, h1, i1, j1]])
            new_pred_1 = regression_model.predict(new_sample_1)[0]

            st.write('## :green[Predicted resale price:] ', np.exp(new_pred_1))
