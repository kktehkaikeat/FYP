import streamlit as st
import csv
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()



st.title("Upload your File here")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    TextFileReader = pd.read_csv(uploaded_file, chunksize=1000)
    dfList = []
    for df in TextFileReader:
        dfList.append(df)

    df = pd.concat(dfList,sort=False)


    st.write(df)
    df['datetime'] = pd.to_datetime(df.Date.astype(str)+' '+df.Time.astype(str))
    df["Label"] = df["Level"].apply(lambda x: int(x != "INFO"))
    df['timestamp'] = df["datetime"].values.astype(np.int64) // 10 ** 9

    ax = sns.countplot(x ='Level', data = df)
    ax.set(title='Number of Normal (0) and Abnormal Sequences (1) ')
    for p in ax.patches:
        height = p.get_height()
        ax.text(x = p.get_x()+(p.get_width()/2), 
        y = height+10,
        s = '{:.0f}'.format(height), 
        ha = 'center') 
    plt.show()
    plt.savefig('count_plot')
    st.write("Level towards Count plot")
    st.image("count_plot.png")
    plt.figure()

    df_normal = df[df["Label"] == 0]
    df_abnormal = df[df["Label"] == 1]

    
    bx = sns.countplot(x ='Port Number', data = df_abnormal, order=df_abnormal.value_counts(df_abnormal['Port Number']).iloc[:3].index)
    bx.set(title='Top 3 port number that contains anomaly')
    for p in bx.patches:
        height = p.get_height()
        bx.text(x = p.get_x()+(p.get_width()/2), 
        y = height+2,
        s = '{:.0f}'.format(height), 
        ha = 'center') 
        plt.savefig('count_plot_port')
    st.write("Plot Based Port Number")
    st.image("count_plot_port.png")
    plt.figure()

        
    cx = sns.countplot(x ='Module Name', data = df_abnormal, order=df_abnormal.value_counts(df_abnormal['Module Name']).iloc[:3].index)
    cx.set(title='Top 3 Module Name that contains anomaly')
    for p in cx.patches:
        height = p.get_height()
        cx.text(x = p.get_x()+(p.get_width()/2), 
        y = height+2,
        s = '{:.0f}'.format(height), 
        ha = 'center') 
        plt.savefig('count_plot_modulename')
    st.write("Plot Based Module Name")
    st.image("count_plot_modulename.png")
    plt.figure()

    dx = sns.countplot(x ='Time', data = df_abnormal, order=df_abnormal.value_counts(df_abnormal['Time']).iloc[:3].index)
    dx.set(title='Top 3 Time that contains anomaly')
    for p in dx.patches:
        height = p.get_height()
        dx.text(x = p.get_x()+(p.get_width()/2), 
        y = height,
        s = '{:.0f}'.format(height), 
        ha = 'center') 
        plt.savefig('count_plot_time')
    st.write("Plot Based Time")
    st.image("count_plot_time.png")
    plt.figure()

    ex = sns.countplot(x ='Database', data = df_abnormal, order=df_abnormal.value_counts(df_abnormal['Database']).iloc[:3].index)
    ex.set(title='Top 3 Database that contains anomaly')
    for p in ex.patches:
        height = p.get_height()
        ex.text(x = p.get_x()+(p.get_width()/2), 
        y = height,
        s = '{:.0f}'.format(height), 
        ha = 'center') 
        plt.savefig('count_plot_database')
    st.write("Plot Based Database")
    st.image("count_plot_database.png")
    plt.figure()

