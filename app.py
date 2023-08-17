import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('model.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

company = st.selectbox('Brand', df['Company'].unique())

types = st.selectbox('Type', df['TypeName'].unique())

ram = st.selectbox('Ram (in GB)',[2,4,8,12,16,24,32,64])

weight = st.number_input('weight')

touchscreen = st.selectbox('Touchscreen',['Yes', 'No'])

ips = st.selectbox('IPS',['Yes', 'No'])

screen_size = st.number_input('Screen_Size')

resolution = st.selectbox('Screen Resolution',['1366x768','1600x900','1920x1080','2304x1440','2560x1440','1560x1600','2880x1800'])

cpu = st.selectbox('CPU', df['Brand_Cpu'].unique())

hdd = st.selectbox('HDD',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU', df['Brand_Gpu'].unique())

os = st.selectbox('OpSys', df['OS'].unique())

X_res = int(resolution.split('x')[0])
Y_res = int(resolution.split('x')[1])
ppi = (((X_res**2) + (Y_res**2))**0.5)/screen_size

if st.button('Predict Price'):
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
        
    if ips == 'Yes':
        ips =  1
    else:
        ips = 0

query = np.array([company,types,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

query = query.reshape(1,12)
st.title("predicted in dollar : $." + str(int(np.exp(pipe.predict(query)[0]))))