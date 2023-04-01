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


def future():
    
    # Write the title
    st.title(
        "Majority of Filipinos have not saved for Old Age"
    )
    st.markdown(
        "**58.4%** of Filipinos have not set aside money for Old Age in the past year."
    )
      
    # Load data
    data = load_data()

    # extract Philippine data
    philippine_data = data[
        data['economy'] == 'Philippines'
        ]

    # Saved for old age = fin16
    # Yes, means saved in the past year(past 12 months, according to the survey questinnaire, not previous year)

    # groupy by those who saved vs those who didn't
    saved_for_old_age = philippine_data.groupby(['fin16']).agg(count = ('wpid_random','count'))

    # add percentage column
    saved_for_old_age['percentage'] = saved_for_old_age/len(philippine_data)

    # Change indices to be more meaning full
    saved_for_old_age_indices = ['Saved', 'Not Saved']
    saved_for_old_age.index = saved_for_old_age_indices

    labels = saved_for_old_age.index

    #tab20c = plt.get_cmap('tab20c')
    tab10_colors = sns.color_palette('tab10', 8).as_hex()
    tab_orange = tab10_colors[1]
    tab_gray = tab10_colors[7]

    label_color = {'Yes': tab_orange,'No': tab_gray}
    # Create subplots: use 'domain' type for Pie subplot
    fig = px.pie(saved_for_old_age, values='count', names=saved_for_old_age.index,
             title='% of Filipinos who saved for old age in the past year',color_discrete_sequence= ['red','green'], 
             labels=saved_for_old_age.index)
    fig.update_traces(textinfo='label+percent')
    fig.update_layout( height=500, margin=dict(l=50, r=50, t=50, b=50), uniformtext= {
        "mode": "hide",
        "minsize": 20
        }, showlegend=False)

    #fig.update_traces(domain=dict(x=[0, 1]))
    st.plotly_chart(fig)
    ##################################################

    st.markdown(
        """
        While this figure may seem discouraging, it is worth noting that a significant portion of the population was able to save for old age, \
        especially when compared to several other countries in the East Asia & Pacific (excluding high income) region, such as Cambodia, Mongolia, Lao PDR, Indonesia \
        and Myanmar, where less than a third of the population saved for old age, the percentage of savers in the Philippines (41.6%) is relatively high. \
        In terms of those who saved in the past year, **the Philippines still ranked third in the region**, behind Malaysia (54.8%) and Thailand (55.6%), which had higher percentages.
        """
    )

    fin16 = data.query('regionwb == \'East Asia & Pacific (excluding high income)\'').groupby(['economy', 'fin16']).size().unstack(fill_value=0)
    fin16['yes_percentage'] = (fin16[1]/(fin16[1]+fin16[2])*100).round(1)
    fin16.sort_values('yes_percentage', ascending = False, inplace=True)
    fin16['yes_percentage_string'] = fin16['yes_percentage'].astype(str) + '%'
    #set figsize
    #create barplot
    sns.set_style(style='white')   #try
    fig, ax = plt.subplots(figsize=(10, 6))

    cols = ['#FF8000' if (y == 'Philippines') else '#ffcc99' for y in fin16.index]
    # Run bar plot
    sns.barplot(
        fin16['yes_percentage'],
        fin16.index,
        palette=cols,
        orient='h'
    )

    # Set title
    plt.title('Top EA&P Countries who saved or set aside money for old age in the past year', size=22)

    # Set labels
    plt.xlabel('% Population')
    plt.ylabel('Countries')

        #3. personalize axis  
    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)
    ax.set_xlabel("% population", fontsize=20)
    ax.set_ylabel("Countries", fontsize=20)
    ax.set_facecolor('white')
    ax.bar_label(ax.containers[0],labels=fin16['yes_percentage_string'].to_list(), padding=2, size=20)
    ax.axes.xaxis.set_ticklabels([])
    ax.set_xlim([0,65])
    ax.tick_params(bottom=False)

    # Show the data
    st.pyplot(fig)

    
    st.subheader(
        "Only the richest Filipinos saved for their future"
    )
    st.markdown(
        """
        Less than 30% of low-income Filipinos have saved for Old Age in the past year. Even in the second richest group, only less than half have saved. **Only the richest group had a majority of individuals who saved in the past year.**
        """
    )

    income_mapping = {1: 'poorest', 2: 'poor', 3:'middle class', 4: 'rich', 5: 'richest'}
    philippine_data['income'] = philippine_data[['inc_q']].replace({'inc_q':income_mapping})
    fin16_ph_income = philippine_data.groupby(['income', 'fin16']).size().unstack(fill_value=0)
    fin16_ph_income['yes_percentage'] = fin16_ph_income[1]/(fin16_ph_income[1]+fin16_ph_income[2])*100
    fin16_ph_income['no_percentage'] = fin16_ph_income[2]/(fin16_ph_income[1]+fin16_ph_income[2])*100
    fin16_ph_income['% difference'] = fin16_ph_income['yes_percentage'] - fin16_ph_income['no_percentage']
    fin16_ph_income.sort_values('% difference', ascending = True, inplace=True)

 
    
    fin16_ph_income['%string']=fin16_ph_income['% difference'].round(2).astype(str) + '%'
    #st.dataframe(fin16_ph_income)
    


    sns.set_style(style='white')

  
    # Set figure size
    fig3, ax2 = plt.subplots(figsize=(10,6))
    #cm = plt.get_cmap('tab20c')

    cols = ['#CC0000','#CC0000','#CC0000','#CC0000','#DF8020']
    # Run bar plot
    sns.barplot(x=fin16_ph_income.index, y = '% difference', data=fin16_ph_income,
                palette=cols, ax=ax2)    
    # Set labels
    ax2.tick_params(axis='x', labelsize=15)
    ax2.tick_params(axis='y', labelsize=15)
    ax2.set_xlabel('Income Group',fontsize=17)
    ax2.set_ylabel('',fontsize=17)
    ax2.set_ylim(-62, 40)
    ax2.set_facecolor('white')

    ax2.set_title('Difference of with savings and without savings for Old Age', fontsize=18)  # add a title

    ax2.bar_label(ax2.containers[0],labels=fin16_ph_income['%string'].to_list(), padding=2, size=15)
    ax2.axes.yaxis.set_ticklabels([])

    # Show figure
    st.pyplot(fig3) 


load_data()
future()
