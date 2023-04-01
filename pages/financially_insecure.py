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

def financially_insecure():

    # Load data
    data = load_data()

    philippine_data = data[
        data['regionwb'] == 'East Asia & Pacific (excluding high income)'
        ]
    
    st.title("Filipinos are financially insecure.")
    #st.markdown
    # INSERT GRAPH 
    st.subheader(
        """20.80% of Filipinos are very worried about all four financial issues. Filipinos identified medical expenses as their biggest financial worry"""
        )

    st.markdown(
        """Looking at another dimension of financial well-being that is the anxiety or worry that people feel about their financial lives. This section specifically examines if Filipinos were worried about their finances, how worried they were about four common issues, and which issue they worry about the most. 
        In this study, about 20.8% of Filipinos are very worried on all four financial issues and the specific issue they are most worried about is not having enough money to pay for medical costs in case of a serious illness or accident.  
        """     
        )   
    # Partition the page into 2
    col1, col2 = st.columns(2)
    # Display metric in column 1
    col1.metric(
        label='', value=str('28.80%')
    )
    col1.markdown("""of Filipinos are very worried about all four financial issues.""")

    # Display metric in column 1
    col2.metric(
        value=str('Medical Expenses'), label=''
        )
    col2.markdown("Biggest financial worry of Filipinos")

    philippine_data = data[
        data['economy'] == 'Philippines'
        ]
    # Group the data and apply aggregations

    def fin_worry(row):
        if row['fin45']==1:
            return 'Old Age'
        elif row['fin45']==2:
            return 'Medical Cost'
        elif row['fin45']==3:
            return 'Monthly Expense or Bills'
        elif row['fin45']==4:
            return 'School or Education Fees'
        else:
            return 'unknown/no answer'

    data['FinancialWorry'] = data.apply(fin_worry, axis=1)
    # Fetch Philippine data
    philippine_data = data[
        data['economy'] == 'Philippines'
        ]
    # Group the data and apply aggregations

    grouped_dataph = philippine_data.groupby(['economy', 'FinancialWorry']).agg(
    total_population=('wpid_random', 'count')
    ).reset_index()
    grouped_dataph['% most worried'] = grouped_dataph['total_population'] / 1000 *100
    grouped_dataph=grouped_dataph.sort_values('% most worried',ascending=False)

    # Compute debit card ownership in %
    sns.set(font_scale=2)
    fig, ax = plt.subplots(figsize=(10, 6))
    cols = ['#DF8020' if (y == 'Medical Cost') else '#adbdc4' for y in grouped_dataph.FinancialWorry]
    sns.barplot(x="% most worried", y="FinancialWorry", data=grouped_dataph, ax=ax, orient='h', palette=cols)
    st.pyplot(fig)

load_data()
financially_insecure()
