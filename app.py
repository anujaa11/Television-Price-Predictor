import streamlit as st
import pickle
import numpy as np
import sklearn


pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Television Predictor")

# brand
Brand = st.selectbox('Brand', df['Brand'].unique())

# Resolution Type
Resolution_Type = st.selectbox('Resolution Type', df['Resolution_Type'].unique())

resolution = st.selectbox('Resolution in Pixel', ['1280x720', '1920x1080', '3840x2160', '7680x4320'])

# Display size
display = st.number_input('Display size (inch)')

# launch_year
launch_year = st.selectbox('Launch Year', df['launch_year'].unique())

# smart_tv
smart_tv = st.selectbox('Smart TV', ['No', 'Yes'])

# os
os = st.selectbox('Operating System', df['os'].unique())

# usb_count
usb_count = st.selectbox('USB', [1, 2, 3])

# hdmi_count
hdmi_count = st.selectbox('HDMI', [1, 2, 3, 4])

# screen_type
screen_type = st.selectbox('Screen Type', df['screen_type'].unique())
if st.button('Predict Price'):
    if smart_tv == 'Yes':
        smart_tv = 1
    else:
        smart_tv = 0

    X_Pixel = int(resolution.split('x')[0])
    Y_Pixel = int(resolution.split('x')[1])
    Pixels_per_Inch = ((X_Pixel * Y_Pixel) / display)

    query = np.array([Brand, launch_year, Resolution_Type, os, screen_type, smart_tv, usb_count, hdmi_count, Pixels_per_Inch])

    query = query.reshape(1, 9)

    st.title(int(np.exp(pipe.predict(query)[0])))
