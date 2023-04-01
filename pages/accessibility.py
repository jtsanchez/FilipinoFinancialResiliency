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

def accesibility():
    st.title(
        "Accesibility of Financial Services"
    )

    st.subheader(
        "Encourage savings by making bank accounts more accessible"
    )

    st.markdown("""
        We suggest implementing **financial education programs and incentives**, **reducing bank fees**,\
        as well as **simplifying account opening procedures** to promote opening of bank accounts.
    """)

    st.markdown(
        "Filipinos that have accounts at financial institutions such as banks are more likely to have saved in the past year, and has, on average, decrease in financial worry over those without accounts."
    )

    data  = load_data()

    # Filter Philippine data
    philippine_data = data[
        data['economy'] == 'Philippines'
    ]

    saved_mapping = {0: 'not saved in the past year', 1: 'saved in the past year'}
    fin16_mapping = {1: 'saved in the past year', 2: 'not saved in the past year', 3: 'don\'t know', 4: 'refused'}
    account_fin_mapping = {0: 'no FI account', 1: 'has FI account'}
    saved_name = 'saved in the past year'
    fin16_name = 'saved for old age'
    account_fin_name = 'FI account'
    philippine_data[saved_name]=philippine_data['saved'].map(saved_mapping)
    philippine_data[fin16_name]=philippine_data['fin16'].map(fin16_mapping)
    philippine_data[account_fin_name]=philippine_data['account_fin'].map(account_fin_mapping)
    grouped_data = philippine_data.groupby([account_fin_name,saved_name]).size().unstack()

    row_totals = grouped_data.sum(axis=1)
    df_percent = grouped_data.div(row_totals, axis=0)*100
    
    sns.set(font_scale=2)
    fig, ax = plt.subplots(figsize=(10, 6))

    cols = ['green', 'red']
    sns.set_style("whitegrid")
    g1 = sns.barplot(y='saved in the past year', x=df_percent.index.tolist(), data=df_percent, ax=ax, palette=cols)
    #g1.set_ylim(0,100)
    g1.set(title='Savers with vs without FI account (%)')  # add a title
    g1.set(ylabel=None)  # remove the axis label

    for p in g1.patches:
        height = p.get_height()
        if height > 0:
            g1.text(p.get_x()+p.get_width()/2., height, '{:.1f}%'.format(height), ha="center", fontsize=19)

    ax.set_facecolor('white')

    ax.axes.yaxis.set_ticklabels([])   #to remove y axis labels since bar has labels already

    st.pyplot(fig)

    st.markdown(
        "For the low to middle income, access to financial institutions may have no real effect on their financial worries but at least it allows them access to more funds through loans."
    )


    col1, col2 = st.columns(2)
    
    with col1:
        financially_worried_mapping = {1: 'worried', 0: 'not worried'}
        account_fin_mapping = {0: 'no FI account', 1: 'has FI account'}
        inc_q_mapping = {1: 'poorest', 2: 'poor', 3: 'middle class', 4: 'rich', 5: 'richest'}
        inc_q_name = 'income group'
        account_fin_name = 'FI account'
        philippine_data[account_fin_name]=philippine_data['account_fin'].map(account_fin_mapping)
        philippine_data[inc_q_name] = philippine_data['inc_q'].map(inc_q_mapping)
        financially_worried=(philippine_data['fin44a']<=2) | (philippine_data['fin44b']<=2) | (philippine_data['fin44c']<=2) | (philippine_data['fin44a']<=2)
        philippine_data['financially worried'] = np.where(financially_worried, 1, 0)
        philippine_data['financially worried'] = philippine_data['financially worried'].map(financially_worried_mapping)
       
        grouped_data = philippine_data.groupby(['inc_q',account_fin_name,'financially worried']).size().unstack(fill_value=0)
        row_totals = grouped_data.sum(axis=1)
        df_percent = grouped_data.div(row_totals, axis=0)*100
        print(df_percent)
        df_percent= df_percent[['worried']]
        df_percent = df_percent.reset_index()

        df_percent[inc_q_name]=df_percent['inc_q'].map(inc_q_mapping)
        sns.set(font_scale=2)
        fig, ax = plt.subplots(figsize=(10, 6))

        sns.set_palette(['green', 'red'])

        g1 = sns.barplot(y='worried', x=inc_q_name, data=df_percent, hue='FI account', ax=ax)
        g1.set(title='Financially worried with vs without FI account (%)')  # add a title
        g1.set(ylabel=None)  # remove the axis label
        g1.set_ylim(80,104)
        g1.legend(loc='upper left', bbox_to_anchor=(0.575, 1.03), ncol=1)
        for p in g1.patches:
            height = p.get_height()
            if height > 0:
                g1.text(p.get_x()+p.get_width()/2., height, '{:.1f}%'.format(height), ha="center", fontsize=16)
        
        ax.set_facecolor('white')
        ax.axes.yaxis.set_ticklabels([])   #to remove y axis labels since bar has labels already

        st.pyplot(fig)
    with col2:
        borrowed_mapping = {0: 'did not borrow', 1: 'borrowed'}
        borrowed_name = 'borrowed in the past year'
        philippine_data[borrowed_name]=philippine_data['borrowed'].map(borrowed_mapping)
        grouped_data = philippine_data.query('inc_q <= 3').groupby([account_fin_name,borrowed_name]).size().unstack()
        row_totals = grouped_data.sum(axis=1)
        df_percent = grouped_data.div(row_totals, axis=0)*100
        sns.set(font_scale=2)
        fig, ax = plt.subplots(figsize=(10, 6))

        cols = ['green', 'red']
        sns.set_style("whitegrid")
        g1 = sns.barplot(y='borrowed', x=df_percent.index.tolist(), data=df_percent, ax=ax, palette=cols)
        #g1.set_ylim(0,100)
        g1.set(title='Low to middle income borrowers with vs without FI account (%)')  # add a title
        g1.set(ylabel=None)  # remove the axis label

        for p in g1.patches:
            height = p.get_height()
            if height > 0:
                g1.text(p.get_x()+p.get_width()/2., height, '{:.1f}%'.format(height), ha="center", fontsize=16)
        ax.set_facecolor('white')

        ax.axes.yaxis.set_ticklabels([])   #to remove y axis labels since bar has labels already
        st.pyplot(fig)
accesibility()
