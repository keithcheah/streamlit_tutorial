#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import streamlit as st
import pickle
import sklearn

# Function to predict output based on user inputs
def predict_output(input_df):
    # Placeholder implementation
    # Replace this with your trained model's prediction logic
    
    #LNM_model = pickle.load(open('sample_model.sav', 'rb'))
    LNM_model = pickle.load(open('rnd_clf_opt_rndcv.sav', 'rb'))
    print(type(LNM_model))

    # OUTPUT = predicted probability of LNM
    pred = float(LNM_model.predict(input_df))
    return pred
    
    # dummy "model" for dummy deployment app - June 2023
    #return input_df.sum(axis=1)

def main():
    # Set page title
    st.title("Numerical Output Prediction")

    # Add input fields for user to enter feature values
    pirads = st.selectbox("PIRADS score", options=[1, 2, 3, 4, 5])
    age = st.number_input("Age", min_value=0, max_value=120, value=60)
    psa = st.number_input("PSA (ng/mL)", min_value=0.0, value=1.0)
    vol = st.number_input("Prostate volume (cm^3)", min_value=10.0, max_value=200.0, value=10.0)
    adeno = st.radio("Adenopathy? (0=No/1=Yes)", options=[0, 1])
    grade = st.selectbox("Biopsy grade", options=[1, 2, 3, 4, 5])
    white = st.radio("Race: white? (0=No/1=Yes)", options=[0, 1])
    
    #race = st.radio("Race", ("White", "Black", "Asian", "Unknown/Other"), horizontal = True)
    #white = (race == "White") * 1
    #black = (race == "Black") * 1
    #asian = (race == "Asian") * 1
    #other = (race == "Unknown/Other") * 1
    
    input_dict = {"P_Score": pirads, "age_rp": age, "PSA": psa,
                 "prostate_volume": vol, "adenopathy": adeno, 
                 "grade_prostate_bx": grade, "white_race": white}

    input_df = pd.DataFrame([input_dict])
    
    center_button = st.button("Estimate")
    
    if center_button:

        # Predict the output based on user inputs
        output = predict_output(input_df)
   
        # Display the predicted output
        st.write("Lymph node metastasis?", output)

if __name__ == "__main__":
    main()

