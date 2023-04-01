from st_pages import add_indentation
add_indentation()

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
#add in libraries
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

sns.set()

def load_data():
    # Load the data
    data = pd.read_csv(
        "micro_world.csv",
        encoding='ISO-8859-1'
    )
    return data

def financial_support():
    st.title(
        "Financial Support Prioritization"
    )


    st.subheader("Prioritize Financial Support to Filipinos with Low Income and Low Education")

    st.markdown("As lack of money remains the primary reason for inability of Filipinos to save, it is critical to have financial support programs focused on the identified demographic without savings.")

    st.image("pic.JPG")

    st.markdown("""

    The target demographic was profiled using chi-squared test at p=0.05 and k-modes clustering. The following clusters were identified:
    """)

    # create an empty dataframe
    df = pd.DataFrame(columns=['Income Quartile', 'Education', 'Savings', '% Population'])

    # add data to the dataframe
    df.loc[0] = ['middle', 'secondary','with savings','38.6%']
    df.loc[1] = ['richest', 'completed tertiary or more','with savings','19.1%']
    df.loc[2] = ['rich', 'secondary','with savings','17.8%']
    df.loc[3] = ['poorest', 'completed primary or less','no savings','15.9%']
    df.loc[4] = ['poor', 'secondary','no savings','8.6%']

    st.dataframe(df)

    st.markdown("No significant relationship with savings/no savings were found on the gender, employment status, and age group of the respondents")


load_data()
financial_support()
