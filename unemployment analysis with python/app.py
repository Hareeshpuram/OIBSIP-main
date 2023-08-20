import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="unemployment in india dashboard",page_icon=":bar_chart:",layout="wide")

@st.cache_data
def getdata():
    df=pd.read_csv('final_unemployementdata.csv')
    return df
df=getdata()

st.sidebar.header("Filters")
state=st.sidebar.multiselect("select state",options=df['Region'].unique(),default=df['Region'].unique())
month=st.sidebar.multiselect("select month",options=df['month'].unique(),default=df['month'].unique())

df_selection=df.query("Region==@state & month==@month")

st.title(":bar_chart: UnEmployment in India Dashboard (May2019-June2020)")

avgunemp=df_selection[" Estimated Unemployment Rate (%)"].mean()
avgunemp=round(avgunemp,2)
highunemp=df_selection.groupby('month')[' Estimated Unemployment Rate (%)'].sum().reset_index('month').sort_values(by=' Estimated Unemployment Rate (%)',ascending=False).head(1)
highunemp=highunemp['month'].to_list()[0]



l,r=st.columns(2)
with l:
    st.subheader("AVG Unemployment rate")
    st.subheader(f"{avgunemp}")
with r:
    st.subheader("high Unemployment rate (Month-year)")
    st.subheader(f"{highunemp}")   


unemp=px.bar(df_selection,x="Region",y=" Estimated Unemployment Rate (%)",title="<b>Estimated Unemployment Rate (%) by state</b>")    
st.plotly_chart(unemp,use_container_width=True)


top10=df_selection.groupby(['Region'])[' Estimated Unemployment Rate (%)'].sum().reset_index()
top10=top10.sort_values(by=[' Estimated Unemployment Rate (%)'],ascending=False)
top10=top10.head(10)
top10un=px.bar(top10,x='Region',y=' Estimated Unemployment Rate (%)',title="<b>Top 10 Estimated Unemployment Rate (%) by state</b>")
st.plotly_chart(top10un,use_container_width=True)


em=px.bar(df_selection,x="Region",y=" Estimated Employed",title="<b>Estimated employment by state</b>")
st.plotly_chart(em,use_container_width=True)    


top10e=df_selection.groupby(['Region'])[' Estimated Employed'].sum().reset_index()
top10e=top10e.sort_values(by=[' Estimated Employed'],ascending=False)
top10e=top10e.head(10)
topem=px.bar(top10e,x='Region',y=' Estimated Employed',title="<b>Top 10 Estimated Employment by state</b>")
st.plotly_chart(topem,use_container_width=True)

#Estimated Total Labour Participation Rate (%)by state
par=px.bar(df_selection,x='Region',y=' Estimated Labour Participation Rate (%)',title="<b> Estimated Labour Participation Rate (%) </b>")
st.plotly_chart(par,use_container_width=True)

lg,rg=st.columns(2)
with lg:
    month=df_selection.groupby('month')[' Estimated Unemployment Rate (%)'].sum().reset_index()
    month=month.sort_values(by=['month'],key=lambda x:pd.to_datetime(x,format='%m-%y'))
    mon=px.line(month,x='month',y=' Estimated Unemployment Rate (%)',title="<b> Estimated Unemployment Rate (%) by month-year</b>")
    st.plotly_chart(mon,use_container_width=True)
with rg:
    ar=df_selection.groupby(['Area'])[' Estimated Unemployment Rate (%)'].sum().reset_index()
    area=px.bar(ar,x='Area',y=' Estimated Unemployment Rate (%)',title="<b> Estimated Unemployment Rate (%) by Area </b>") 
    st.plotly_chart(area,use_container_width=True)




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


