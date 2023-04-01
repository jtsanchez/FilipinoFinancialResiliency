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

def summary():
    # Write the title
    st.title(
        "SUMMARY"
    )
    st.subheader(
        """
        **GENERAL CONCLUSION:** Filipinos are ready with short term savings, but not for emergencies and old age. Support should be prioritized to low-income and low-education Filipinos.
        """
    )



    # Partition the page into 2
    col1, col2 = st.columns(2)


    # Display text in column 1
    col1.markdown("""
    :flag-ph: \n 
    Majority of Filipinos (64.5%) have savings; Ranks 4th in East Asia & Pacific region and 1st for lower middle income group in EA&P. \n\n
    :female-doctor: \n
    Medical expenses cause the biggest financial worry among Filipinos \n
    :older_man: \n
    Less than half (41.6%) of Filipinos have set aside money for long-term/old Age since the past year \n
    :heavy_multiplication_x: :mortar_board: \n
    Filipinos in the lowest 40% income quintile and with secondary education and less are less likely to have savings.
 """)

 

    # Display text in column 2
    col2.markdown("""
    :moneybag: \n
    Most Filipinos with savings come from high-income households. Majority of low-income Filipinos and almost half of the middle class have no savings \n
    :family: \n
    More Filipinos will go to their families and friends than their own savings when there’s an emergency \n
    :money_with_wings: \n
    Lack of money and expensive bank fees are the top reasons that hinder Filipinos from saving. \n

    
    """)




    st.subheader(
        """
        **RECOMMENDATION:** Implement rules and regulations that promote and support financial preparedness among Filipinos
        """
    )
    st.markdown(
        """

        :heavy_check_mark: Prioritize financial support to Filipinos with low Income and low Education

        :heavy_check_mark: Regulations to lessen/remove bank fees for people incapable of maintaining the default amount

        :heavy_check_mark: Government partnerships with banks to enable affordable savings programs and microinsurance access for low-income Filipinos

        :heavy_check_mark: Government support on emergency funds for Filipinos

        :heavy_check_mark: Improve government support on medical expenses

        
        
    
        **Recommendations on further analysis:** 
        :bar_chart:  Survey improvements- data with equal distribution per income quintile for more representative findings
        """ 
    )


load_data()
summary()
