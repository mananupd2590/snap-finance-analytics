#!/usr/bin/env python
# coding: utf-8

# Task 4: Create a view with a graph to compare the used dollars amount by Marketing name, and color by spend amount.

import pandas as pd
from sqlalchemy import create_engine

# I coded the first part in SQL because it was easier to analzye there first on how I want my chart to look

# Set up a connection to the local MySQL database
engine = create_engine("mysql+pymysql://root:abc1234@localhost:0000/snap_fin")
conn = engine.connect()

# Load SQL Query and read from .sql file
with open('path/Task4.sql', 'r') as file:
    sql_query = file.read()
df = pd.read_sql(sql_query, conn)

# ---------------------------------------------------------
# VISUALZATION 1: Bar Plot — Conversion Rate by Campaign
# ---------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# Create a bar chart showing the conversion rate (%) by marketing campaign
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='marketing_name', y='conversion_rate_percentage', palette='viridis')

# Style the plot for clarity
plt.xticks(rotation=45)
plt.title('Campaign Conversion Rate (%) by Marketing Name')
plt.ylabel('Conversion Rate (%)')
plt.xlabel('Marketing Name')
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# VISUALIZATION 2: Grouped Bar Plot — Total Spend vs Dollars Used
# ---------------------------------------------------------

import numpy as np
import matplotlib.ticker as ticker

x = np.arange(len(df))
width = 0.35

# Set up the side-by-side bar chart
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width/2, df['total_spend'], width, label='Total Spend')
ax.bar(x + width/2, df['total_dollars_used'], width, label='Dollars Used')

ax.set_xticks(x)
ax.set_xticklabels(df['marketing_name'], rotation=45, ha='right')
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
ax.set_ylabel('Amount ($)')
ax.set_title('Total Spend vs Dollars Used by Campaign')
ax.legend()
plt.tight_layout()
plt.show()
