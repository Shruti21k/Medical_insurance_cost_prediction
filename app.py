import streamlit as st
import pandas as pd
import pickle
import numpy as np


# Customizing the layout
page_bg_img = f'''
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-size: cover;
    background-attachment: fixed;
    background-image: url('https://cdn.discordapp.com/attachments/1154429779982942258/1200487595138887770/Untitled_design_2.jpg?ex=65c65c32&is=65b3e732&hm=2d6dad3ca643b54d0ce8ccc66d69ba7df9e512ae4094ad6291b58cfdbec340c5&');
    font-family: Roboto;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stMarkdownContainer"]{{
    color: black;
    font-family: Roboto;
    font-size: 30px;
    align-items: center;
}}

[data-testid="baseButton-secondary"]{{
    background-color: red;
    border-radius: 15px;
}}

[data-testid="StyledLinkIconContainer"] {{
    color: #5C4033;
    }}

[data-testid="stColumns"] {{
    background-color: white;
    color: brown;
    border-radius: 2px;
}}

[data-testid="stNotification"]{{
    border-radius: 15px;
    font-family: Roboto;
}}
</style>
'''


st.markdown(page_bg_img, unsafe_allow_html=True)
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
# Container for the main content
with st.container():
    # Centered heading
    st.title("Know your Insurance Amount Now!")

    # Two containers for questions
    col1, col2 = st.columns(2)

    # Left container
    with col1:
        # st.subheader("Questions")
        age = st.number_input('Age', min_value=19, max_value=30, step=1, value=25)
        sex = st.radio('Gender', options=('Male', 'Female'))
        children = st.number_input('Number of Children', min_value=0, max_value=10, step=1, value=0)
        st.write('')

    # Right container
    with col2:
        # st.subheader("Questions")
        bmi = st.number_input('BMI')
        smoker = st.radio('Do you Smoke?', options=('Yes', 'No'))
        region = st.selectbox('Region', options=('Northwest', 'Northeast', 'Southwest', 'Southeast'))
        st.write('')

    with st.container():
        # Centered "Get Quote" button
        ex_col_l, ex_2, button_col, ex_col_r = st.columns([0.7, 0.7, 1 ,1])

        with button_col:
            st.write('')
            
            if st.button('Get Quote'):
                temp_df = pd.DataFrame(data=[[age, sex.lower(), bmi, children, smoker.lower(), region.lower()]],
                                    columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
                model = pickle.load(open('insurance_model.pkl', 'rb'))
                y_pred = model.predict(temp_df)
                st.success(f'Your Insurance Quote is {int(np.exp(y_pred)[0])}$', icon="✅")
