# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 00:54:29 2024

@author: HP
"""

import streamlit as st
import joblib
import os

def main():
    
    html_temp = """
    <div style= "background-color:blue; padding:12px; border: 3px solid white; border-radius: 10px">
    <h2 style = "color:white; text-align:center; font-family: 'Arial', sans-serif">Predicting Oil Viscosity Status</h2> 
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Ensure the model file is in the same directory as app.py
    model_path = os.path.join(os.path.dirname(__file__), 'OilViscosity1Model_rf.joblib')
    model = joblib.load(model_path)  
    
    p1 = st.selectbox('Select temperature', options=[100])
        
    p2 = st.selectbox('Select the Year', options=[2024])
    
    p3 = st.slider("Select month", 1, 12)
    
    p4 = st.number_input("Date of Prediction:", step=1, format="%d", value=1, max_value=31)
    
    if p1 == 100:
        OilStandard = 15.3
    else:
        OilStandard = 115
    
    pred = model.predict([[p1, p2, p3, p4]])
    pred_value = round(pred[0], 2)
    
    Viscosity = ((pred_value / OilStandard) - 1) * 100
    ViscosityPct = round(Viscosity, 2)
        
    if st.button("Predict"):
        
        # Determine the status based on the prediction value 
        if -10 <= ViscosityPct <= 10:
            status = 'Normal'
        elif -30 <= ViscosityPct <= 30:
            status = 'Warning'
        else:
            status = 'Problem'
        
        st.success(f'The Predicted value of Oil Viscosity% on {p4}/{p3}/{p2} is : {ViscosityPct}')
        
                   
        st.success(f'The Status of Oil Viscosity on {p4}/{p3}/{p2} will be : {status} ')
        
        st.info("""
                   - Warning Range : -10% to +10%
                   - Danger Range : -30% to +30%
                   
                   """)

if __name__ == '__main__':
    main()
