import streamlit as st
import pandas as pd
import numpy as np 

st.set_page_config(
    page_title = 'Streamlit Sample Dashboard Template',
    page_icon = '✅',
    layout = 'wide'
)

df = st.session_state["df"]
df_prediction_abnormal =  st.session_state["df_prediction_abnormal"]
df_abnormal = st.session_state["df_abnormal"] 

st.markdown("## Level from Imported Data")

# kpi 1 

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.markdown("**Number Of Info**")
    number1 = df['Level'].value_counts()['INFO'] 
    st.markdown(f"<h1 style='text-align: center; color: green;'>{number1}</h1>", unsafe_allow_html=True)

with kpi2:
    st.markdown("**Number Of Error**")
    number2 = df['Level'].value_counts()['ERROR']
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number2}</h1>", unsafe_allow_html=True)

with kpi3:
    st.markdown("**Number Of Warning**")
    number3 = df['Level'].value_counts()['WARNING'] 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

st.markdown("<hr/>",unsafe_allow_html=True)


st.markdown("## Result from each model (Precison, Recall and F1)")
chart1, chart2, chart3 = st.columns(3)

with chart1:
    st.image("DTresult.png")

with chart2:
    st.image("LRresult.png")

with chart3:
    st.image("SVMresult.png")



st.markdown("## Anomaly Detection using Decision Tree output")
df_abnormal_predicted = df_abnormal[(df['Module Name'] == 'openerp.modules.graph:') | (df['Module Name'] == 'openerp.sql_db:') | (df['Module Name'] == 'openerp.http:')| (df['Module Name'] == 'openerp.addons.base.ir.ir_ui_view:')| (df['Module Name'] == 'openerp.models:')| (df['Module Name'] == 'openerp.addons.email_template.email_template:')| (df['Module Name'] == 'openerp.addons.base.ir.ir_ui_model:')| (df['Module Name'] == 'openerp.addons.base.ir.ir_mail_server:')| (df['Module Name'] == 'openerp.addons.mail.mail_mail:')]
st.write(df_abnormal_predicted)
 
    # df_normal_predicted = df_prediction_abnormal[df_prediction_abnormal["CatModuleName"] <= 10]
    # st.write(df_normal_predicted)

