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

def title():
    # Write the title and the subheader
    st.title("Financial Resiliency: Assessing Filipino’s monetary preparedness"
    )
    st.subheader(
        """
        Rex | Gian | Pau 
        mentor: Tim
        """
    )
    st.subheader(
        """
        Financial resiliency is a critical aspect of personal finance, and it is particularly relevant in the Philippines, where economic uncertainty and financial instability are common. 
        This study will focus on assessing the monetary preparedness of Filipinos. By dwelling into this topic, we can better understand the challenges that Filipinos face and how can we improve financial preparedness among Filipinos.
        """
    )

    # Load photo
    st.image("peso.jpg")

    # Load data
    data = load_data()

    philippine_data = data[
    data['regionwb'] == 'East Asia & Pacific (excluding high income)'
    ]

    # Display data
    st.markdown("**The Data**")
    st.dataframe(philippine_data)
    st.markdown("Source: Global Findex 2021 from World Bank.")

load_data()
title()