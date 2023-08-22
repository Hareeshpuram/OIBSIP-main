import pickle
import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Car price prediction",page_icon=":car:",layout="wide")

@st.cache_data
def getdata():
    model=pickle.load(open('car_price_prediction_RandomForest.pkl','rb'))
    return model
model=getdata()

st.title('Car Price Prediction')
st.divider()

with st.sidebar:
    st.header(' cars by country:')
    car_brands_by_country = {
        'Italian': ['alfa-romero'],
        'German': ['audi', 'bmw', 'volkswagen','porsche'],
        'American': ['chevrolet', 'dodge', 'buick', 'mercury', 'plymouth'],
        'Japanese': ['honda', 'isuzu', 'mazda', 'mitsubishi', 'nissan', 'subaru', 'toyota'],
        'British': ['jaguar'],
        'French': ['peugeot', 'renault'],
        'Swedish': ['saab', 'volvo']
    }
    
    for country, brands in car_brands_by_country.items():
        st.subheader(f'{country}:')
        for c in brands:
            st.text(f'{c}')
            

    


with st.form('Enter car details'):

    country=st.selectbox('country of origin',options=['Italian', 'German', 'American', 'Japanese', 'British', 'French',
        'Swedish'])
    coun={'Italian':1, 'German':2, 'American':3, 'Japanese':4, 'British':5, 'French':6,
        'Swedish':7}
    inp4=coun[country]


    carbody=st.selectbox('car body',options=['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'])
    carb={'convertible':1, 'hatchback':2, 'sedan':3, 'wagon':4, 'hardtop':5}
    inp1=carb[carbody]

    enginetype=st.selectbox('engine type',options=['dohc','ohcv' ,'ohc' ,'l', 'rotor','ohcf', 'dohcv'])
    engine={'dohc':1 ,'ohcv':2 ,'ohc':3 ,'l':4, 'rotor':5 ,'ohcf':6, 'dohcv':7}
    inp2=engine[enginetype]

    fuelsytem=st.selectbox('Fuel system',options=['mpfi', '2bbl', 'mfi', '1bbl', 'spfi' ,'4bbl', 'idi', 'spdi'])
    fuel={'mpfi':1, '2bbl':2, 'mfi':3, '1bbl':4, 'spfi':5 ,'4bbl':6, 'idi':7, 'spdi':8}
    inp3=fuel[fuelsytem]

    fueltype=st.selectbox('fuel type',options=['gas','diesel'])
    if fueltype=='gas':
        inp5=1
    else:
        inp5=0

    aspiration=st.selectbox('Aspiration',options=['std' ,'turbo'])
    if aspiration=='turbo':
        inp6=1
    else:
        inp6=0    

    drivewheel=st.selectbox('Drive wheel',options=['rwd', 'fwd' ,'4wd'])
    if drivewheel=='fwd':
        inp7=1
        inp8=0
    elif drivewheel=='rwd':
        inp7=0
        inp8=1
    else:
        inp7=0
        inp8=0


    enginelocation=st.selectbox('Engine Location',options=['front' ,'rear'])
    if enginelocation=='rear':
        inp9=1
    else:
        inp9=0

    doornum=st.selectbox(' Number of doors',options=[2,4])
    inp10=int(doornum)

    inp11=float(st.number_input('Wheel base',help='88.6'))

    inp12=float(st.number_input('car length'))

    inp13=float(st.number_input('car width'))

    inp14=int(st.number_input('curbweight'))

    inp15=int(st.selectbox('Cylinder number',options=[2,3,4,5,6,8,12]))

    inp16=int(st.number_input('Engine size'))

    inp17=float(st.number_input('Bore ration'))

    inp18=float(st.number_input('stroke'))

    inp19=int(st.number_input('Horse power'))

    inp20=int(st.number_input('Peak RPM'))


    inp21=int(st.number_input('city mpeg'))

    inp22=int(st.number_input('highway mpeg'))

    sub=st.form_submit_button('Predict')
    if sub:
        input=[inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13,inp14,inp15,inp16,inp17,inp18,inp19,inp20,inp21,inp22]
        input=np.array(input).reshape(1,-1)
        pred=model.predict(input)
        with st.spinner('Predicting'):
            time.sleep(2)
        st.header(f'price predicted: ${round(pred[0],2)}')









footer="""
<br><p> Made by  PURAM HAREESH </p>
<a href='https://www.linkedin.com/in/hareesh-puram-21344a23b'>linkedin</a><br><a href='https://github.com/Hareeshpuram'>Github</a>"""

st.markdown(footer,unsafe_allow_html=True)
hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
            """
st.markdown(hide_st_style,unsafe_allow_html=True)


