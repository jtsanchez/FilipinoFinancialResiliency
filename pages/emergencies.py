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

def emergencies():
    # Write the title
    st.title(
        "Filipinos find it difficult to prepare for emergencies"
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

    # Partition the page into 2
    col1, col2 = st.columns(2)


    # Display metric in column 1
    col1.metric(
        label='% with difficulty in getting emergency funds within 30 days',
        value=str('80.2%')
    )

    # Display metric in column 1
    col2.metric(
        label='% with difficulty in getting emergency funds within 7 days',
        value=str('85.5%')
    )

    
  
    # Difficulty in coming up with emergency funds within 30 days = fin24a

    difficulty_30 = philippine_data.groupby(['fin24a'],dropna = True).agg(count = ('wpid_random','count'))

    difficulty_30['percentage'] = difficulty_30/1000 
    difficulty_30_indices = ['Very Difficult', 'Difficult', 'Not Difficult']

    difficulty_30.index = difficulty_30_indices
    difficulty_30.append(difficulty_30.sum().rename('Total')).style.format({'percentage': '{:.2%}'})

    # Difficulty in coming up with emergency funds within 7 days = fin24b
    difficulty_7 = philippine_data.groupby(['fin24b'],dropna = True).agg(count = ('wpid_random','count'))
    difficulty_7['percentage'] = difficulty_7/1000
    difficulty_7_indices = ['Very Difficult', 'Difficult', 'Not Difficult']
    difficulty_7.index = difficulty_7_indices
    difficulty_7.append(difficulty_7.sum().rename('Total')).style.format({'percentage': '{:.2%}'})

    labels = difficulty_30.index
    label_color = {'Very Difficult':'red', 'Difficult':'orange', 'Not Difficult':'green'}

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels, values=(difficulty_30['percentage']*100).round(2), name="DIFFICULTY", marker_colors=difficulty_30.index.map(label_color),
                         insidetextorientation = "horizontal"),1, 1)
    fig.add_trace(go.Pie(labels=labels, values=(difficulty_7['percentage']*100).round(2), name="DIFFICULTY", marker_colors=difficulty_7.index.map(label_color),
                         insidetextorientation = "horizontal"),1, 2)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.5, hoverinfo="label+percent+name", textinfo='percent+label')

    fig.update_layout(
        title_text="Difficulty in Preparing Emergency Funds within Given Period",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='within 30 days', x=0.14, y=0.5, font_size=20, showarrow=False),
                    dict(text='within 7 days', x=.85, y=0.5, font_size=20, showarrow=False)],
        height=500, margin = dict(l=0,r=0,t=100,b=100), showlegend=False)
    #fig.show()

    st.markdown(
        "Filipinos that find it **very difficult** to get emergency funds increase by **13.8%** as the timeline is shortened from 30 to 7 days"
       
    )

    st.plotly_chart(fig)

    ###end trial

emergencies()

