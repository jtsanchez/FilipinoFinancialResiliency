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

def rely_on_sns():
    
    data = pd.read_csv(
        "micro_world.csv",
        encoding='ISO-8859-1'
    )
    
    philippine_data = data[data['economy'] == 'Philippines']
    st.title("Filipinos often rely on social networks.")
    st.subheader(
        """Around 42.80% of Filipinos opt to borrow from family, relatives or friends rather than in a financial institution or informal savings."""
        )    

    def fin22a1(row):
        if row['fin22a']==1:
            return 'Yes'
        elif row['fin22a']==2:
            return 'No'
        else:
            return 'Unknown/no answer'

    # Fetch Philippine data
    philippine_data = data[data['economy'] == 'Philippines']

    # Group the data and apply aggregations
    grouped_dataph = philippine_data.groupby(['economy']).agg(
        borrowed_fin=('fin22a', lambda x: sum(x==1)),
         borrowed_fam=('fin22b', lambda x: sum(x==1)),
        borrowed_inf=('fin22c', lambda x: sum(x==1)),
         total_population=('wpid_random', 'count')
        ).reset_index()

    grouped_dataph['Financial Institution'] = grouped_dataph['borrowed_fin']*100.0/grouped_dataph['total_population']
    grouped_dataph['Family/Relatives'] = grouped_dataph['borrowed_fam']*100.0/grouped_dataph['total_population']
    grouped_dataph['Informal'] = grouped_dataph['borrowed_inf']*100.0/grouped_dataph['total_population']
    grouped_dataph=grouped_dataph.sort_values('Financial Institution',ascending=False)
    




    #st.dataframe(grouped_dataph)



    sns.set(font_scale=2)
    sns.set_style(style='white')
    fig, ax = plt.subplots(figsize=(10, 6))
    cols = ['#DF8020','#F2CCA6','#F2CCA6']

    # Create plot
    ax = sns.barplot(x=['Family/Relatives','Financial Institution', 'Informal'], 
                 y=[grouped_dataph['Family/Relatives'].values[0], 
                    grouped_dataph['Financial Institution'].values[0], 
                    grouped_dataph['Informal'].values[0]], palette=cols)

    # Set plot title and axis labels
    ax.set_title('% of Population borrowed from different sources')
    ax.set_xlabel('Source of Borrowing')
    ax.set_ylabel('% of Population')

    #for p in ax.patches:
    #        height = p.get_height()
    #if height > 0:
    #        ax.text(p.get_x()+p.get_width()/2., height, '{:.1f}%'.format(height), ha="center", fontsize=12)
    #else:
    #        ax.text(p.get_x()+p.get_width()/2., height-7, '{:.1f}%'.format(height), ha="center", fontsize=12)

    #removed labels coz it only shows for one bar
    st.pyplot(fig)

    st.markdown(
        """It is evident that 4 of 10 Filipinos opt to borrow money from family, relatives, or friends rather than in a financial institution or informal savings. 
        """
        )
    

    st.image("challenges.jpg")
    st.markdown(
        """Supporting the previous statement, it is evident that 4 of 10 Filipinos opt to borrow money from family, relatives, or friends rather than in a financial institution or informal savings. According to the 2021 Financial Inclusion Survey by the Banko Sentral ng Pilipinas, half of adult Filipinos perceived that borrowing from formal institutions was difficult.
Across formal institutions, top reasons provided on the perceived difficulty in borrowing were lack of documentary requirements, insufficient IDs, low salary/income, and not having collateral. 
"""
        )


load_data()
rely_on_sns()
