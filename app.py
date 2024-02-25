import pandas as pd
import pickle as pk
import streamlit as st
import numpy as np

pipe = pd.read_pickle('pipe.pkl')
df = pd.read_pickle("df.pkl")

st.title('Smartphone Price Prediction')

company = st.selectbox('Brand',df['Brand'].unique())

processor = st.selectbox('Processor Brand',df['Processor_Brand'].unique())

cores = st.selectbox('Processor Cores',df['Num_Cores'].unique())

ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

rom = st.selectbox('ROM(in GB)',df['Rom'].unique())

screen_size = st.number_input('Screen Size')

processor_speed = st.number_input('Processor Speed')

charger_speed = st.number_input('Charger Speed')

battery = st.number_input('Battery (in MAH)')

fast_charger = st.selectbox('Fast Charging',['Yes','No'])

G5 = st.selectbox('5 G',['Yes','No'])

nfc = st.selectbox('NFC',['Yes','No'])

Os = st.selectbox('OS',df['OS'].unique())

pixel1= st.number_input('Screen Resolution (pixel 1)')
pixel2= st.number_input('Screen Resolution (pixel 2)')

no_rear_camera = st.selectbox('No of rear camera',df['No_rear_camera'].unique())
no_front_camera = st.selectbox('No of front camera',df['No_front_camera'].unique())

primary_rear = st.number_input('Primary rear camera (in MP)')
primary_front = st.number_input('Primary front camera (in MP)')

if st.button('Predict Price'):

    if G5 == 'Yes':
        G5 = 1
    else:
        G5 = 0

    if nfc == 'Yes':
        nfc = 1
    else:
        nfc = 0

    if fast_charger == 'Yes':
        fast_charger = 1
    else:
        fast_charger = 0


    x = [[G5,nfc,processor,cores,processor_speed,ram,rom,fast_charger,charger_speed,battery,Os,pixel1,pixel2,screen_size,no_rear_camera,no_front_camera,primary_rear,primary_front,company]]
    column = ['has_5G','has_NFC','Processor_Brand','Num_Cores','Processor_Speed','Ram','Rom','fast_charging','charger_speed','Battery','OS','pixel_1','pixel_2','screen_size','No_rear_camera','No_front_camera','Primary_camera','Front_camera','Brand']

    df1 = pd.DataFrame(data=x, columns=column)
    #st.title(df1)
    #st.title(pipe.predict(df1))
    st.title("The predicted price of this configuration is " + str(int(pipe.predict(df1)[0])))





















