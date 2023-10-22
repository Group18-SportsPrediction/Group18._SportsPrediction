#Importing libraries
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image


# loading the model 
pickle_in = open('gb_regressor.pkl', 'rb')
regressor = pickle.load(pickle_in)

# defining the function that make the prediction
def prediction(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,z1):   
   
    prediction = regressor.predict( 
        [[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,z1]]) 
    print(prediction) 
    return prediction 

# main function in which we define our webpage
def main():
      #webpage a title
    st.title("Player rating Prediction")

    "Columns to predict the player rating"

    # The following lines create text boxes
    # user can enter values
    # the data required to make the prediction
    
    #The alphabetical letters represent the the columns names 
    a = st.text_input("potential", 80)
    b = st.text_input("international_reputation", 90)
    c = st.text_input("shooting", 70)
    d = st.text_input("passing", 78)
    e = st.text_input("dribbling", 50)
    f = st.text_input("defending", 30)
    g = st.text_input("preferred_foot_Left", 1)
    h = st.text_input("preferred_foot_Right", 0)
    i = st.text_input("body_type_Lean (170-)", 180)
    j = st.text_input("body_type_Lean (170-185)", 183)
    k = st.text_input("body_type_Lean (185+)", 186)
    l = st.text_input("body_type_Normal (170-)", 169)
    m = st.text_input("body_type_Normal (170-185)", 12)
    n = st.text_input("body_type_Normal (185+)", 186)
    o = st.text_input("body_type_Stocky (170-)", 78)
    p = st.text_input("body_type_Stocky (170-185)", 178)
    q = st.text_input("body_type_Stocky (185+)", 186)
    r = st.text_input("body_type_Unique", 1)
    s = st.text_input("work_rate_High/High", 0)
    t = st.text_input("work_rate_High/Low", 0)
    u = st.text_input("work_rate_High/Medium", 1)
    v = st.text_input("work_rate_Low/High", 0)
    w = st.text_input("work_rate_Low/Low", 0)
    x = st.text_input("work_rate_Low/Medium", 0)
    y = st.text_input("work_rate_Medium/High", 0)
    z = st.text_input("work_rate_Medium/Low", 0)
    z1 = st.text_input("work_rate_Medium/Medium", 0)
    result =""

    # The click button 'Predict' creates,
    # defining the prediction function and store it in the variable result
        
    if st.button("Predict"): 
        result = prediction(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,z1) 
    st.success('The Player rating is {}'.format(result)) 
        

if __name__=='__main__':
    main()