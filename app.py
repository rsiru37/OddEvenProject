import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

def main():
    st.write("""
    # Checks whether the Input Number is Even/Odd
    This app checks even/odd status of the Input Number
    """)
    #Get Input
    st.header('User Input')
    num = st.number_input("NUMBER",min_value=0,max_value=100000,step=1)
    if(num%2 == 0):
      st.write('EVEN NUMBER')
    else:
      st.write('ODD NUMBER')
    
if __name__ == '__main__':
    main()
