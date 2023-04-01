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

def not_financially_independent():
    st.title(
        "Filipinos are Not Financially Independent"
    )

    st.markdown(
         "The respondents were asked what their source of funds will be in the event of an emergency. It was found that more Filipinos are **financially dependent on their friends and family** during emergencies, than their own emergency savings."
    )
        
      
    # Load data
    data = load_data()

    #add col for revised emergency funds source

    #create function
    def emergency_n(row):
        if row['fin24']==1:
            return 'savings'
        elif row['fin24']==2:
            return 'friends/family'
        elif row['fin24']==3:
            return 'work'
        elif row['fin24']==4:
            return 'loan' #borrow from bank/employer/lender
        elif row['fin24']==5:
            return 'sale of assets'
        elif row['fin24']==6:
            return 'other'
        elif row['fin24']==7:
            return 'no money'
        else:
            return 'unknown/no answer'

    data['emergency_funds_source'] = data.apply(emergency_n, axis=1)
    
    # Fetch Philippine data
    philippine_data = data[
        data['economy'] == 'Philippines'
        ]

    # Apply .groupby in data for emergency funds source
    emergency_df=philippine_data.groupby('emergency_funds_source').count()['wpid_random'].to_frame()
    emergency_df['%']=(emergency_df['wpid_random']*100/1000).round(2)
    emergency_df=emergency_df.sort_values('%',ascending=False)
    emergency_df=emergency_df.reset_index()
    emergency_df=emergency_df.rename(columns = {'emergency_funds_source':'Emergency Funds Source','wpid_random':'count'})
    emergency_df['%string']=emergency_df['%'].astype(str) + '%'

    sns.set_style(style='white')
    #set figsize
    fig, ax = plt.subplots(figsize=(10, 6))

    #use orange for bar with max value and grey for all other bars
    cols = ['#FF8000' if (y == 'friends/family') else '#ffcc99' for y in emergency_df['Emergency Funds Source']]

    #create barplot
    #sns.set(font_scale=2)
    #sns.set_style('white')
    sns.barplot(x="%", y="Emergency Funds Source", data=emergency_df,
        palette=cols, ax=ax, orient='h')       

    #sns.despine()

    #3. personalize axis  
    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)
    ax.set_xlabel("% population", fontsize=20)
    ax.set_ylabel("Emergency Funds Source", fontsize=20)

    ax.bar_label(ax.containers[0],labels=emergency_df['%string'].to_list(), padding=2, size=20)
    ax.axes.xaxis.set_ticklabels([])
    ax.set_xlim([0,43])
    ax.tick_params(bottom=False)
 
    

    # Show the figure
    st.pyplot(fig)







load_data()
not_financially_independent()
