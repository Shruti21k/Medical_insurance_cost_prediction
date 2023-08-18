import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.write("## Insurance Calculator")

age = st.number_input('Enter your Age')

sex = st.selectbox(label = 'Select your Gender', 
                   options = ('male', 'female')
                   )

bmi = st.number_input('Enter your bmi')

children = st.number_input('Enter number of children')

smoker = st.selectbox(label = 'Do you Smoke', 
                      options = ('yes', 'no')
                      )

region = st.selectbox(label = 'Enter your Region', 
                      options = ('northwest', 'northeast', 'southwest', 'southeast')
                      )

# Creating DataFrame using values input by user
temp_df = pd.DataFrame(data = [[age, sex, bmi, children, smoker, region]], 
                       columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
                       )

# Loading Model using pickle file
model = pickle.load(open('insurance_model.pkl', 'rb'))

# Creating a button to get prediction
if st.button('Get Quote'):
    y_pred = model.predict(temp_df)
    st.write(f'Your Insurance Quote is {int(np.exp(y_pred)[0])}')