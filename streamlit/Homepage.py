import streamlit as st

st.set_page_config(
    page_title="SitaADS",
)

st.title("Welcome to SitaADS")
st.write("The title can be separated into 2 parts which is “Sita” and “ADS”. “Sita” stands for the company name Sita Group Of Companies and “ADS” stands for the Anomaly Detection for Server Log. With both parts of the title combined together, we can know that the title stands for Anomaly Detection for Server Log by Sita Group Of Companies.")
st.write("To start with the web application , please head to File upload to upload your csv file to get started.")
st.image("sita.jpg")

st.sidebar.success("Please start with Uploading your csv file at !File Upload")

