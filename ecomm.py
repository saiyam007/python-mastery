import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st


def main():
    print("Htis is main oy fule ") 
    pritrntn("checking this is worijngbdfg dhndsnfuiosbnf)
    print("this is streamlit code for forntned)
    st.title('This is my E-commerce Dashboard') # Title of the dashboard
    st.sidebar.title('Upload your file here') # Sidebar to upload the file
    
    uploaded_file = st.sidebar.file_uploader('Upload your file here', type=['csv','xlsx']) # File uploader
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.sidebar.success(f'{uploaded_file.name} File successfully uploaded')
            
            st.subheader(f'Data Overview of {uploaded_file.name} ')
            
            st.dataframe(df)
            
            # st.write(df.head())    
            
            st.subheader('Data Description')
            st.write('**Columns in the dataset**', df.columns)
            st.write('**Shape of the dataset**', df.shape)
            st.write('**Data Types**', df.dtypes)
            st.write('**Missing Values**', df.isnull().sum())
            st.write(df.describe())
            
            plt.figure(figsize=(8, 6))
            sns.countplot(data=df, x='Gender')
            plt.title('Count Plot of Gender')
            
            # Display the plot in Streamlit
            st.pyplot(plt)
            sns.countplot(data=df, x='Age', hue='Gender')
            plt.title('Count Plot of Gender')

            st.pyplot(plt)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)
            print("This is exceeption class")


if __name__ == '__main__':
    main()
    



