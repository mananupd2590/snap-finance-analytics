#!/usr/bin/env python
# coding: utf-8

# TASK-2 : Calculate the average of the approved amount and the average of the amount used and visualize the trend over the submission date.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned applications dataset
df = pd.read_csv('path/applications.csv')


# Prepping up
df['submit_date'] = pd.to_datetime(df['submit_date'])

# column that groups submissions by month
df['submit_month'] = df['submit_date'].dt.to_period('M').astype(str)

# Group the data month-wise and calculate the average approved and used dollar amounts
monthly_trend = df.groupby('submit_month').agg({
    'approved_amount': 'mean',
    'dollars_used': 'mean'
}).reset_index()

# -----------------------------------------------
# VISUALIZATION 1: Separate Line Charts
# -----------------------------------------------

# Create a figure with two vertically stacked subplots (for visual clarity)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# First chart: Monthly average approved amount
ax1.plot(monthly_trend['submit_month'], monthly_trend['approved_amount'], color='blue', marker='o')
ax1.set_title('Average Approved Amount per Month', fontsize=14)
ax1.set_ylabel('Amount ($)', fontsize=12)
ax1.grid(True)

# Second chart: Monthly average dollar usage
ax2.plot(monthly_trend['submit_month'], monthly_trend['dollars_used'], color='green', marker='o')
ax2.set_title('Average Dollars Used per Month', fontsize=14)
ax2.set_ylabel('Amount ($)', fontsize=12)
ax2.set_xlabel('Month', fontsize=12)
ax2.grid(True)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------------------------
# VISUALIZRTION 2 : Combined Chart with Application Volume
# -----------------------------------------------


monthly_summary.columns = ['Month', 'Avg Approved', 'Avg Used', 'Total Applications']

plt.figure(figsize=(14, 6))


plt.plot(monthly_summary['Month'], monthly_summary['Avg Approved'], label='Avg Approved ($)', marker='o')
plt.plot(monthly_summary['Month'], monthly_summary['Avg Used'], label='Avg Dollars Used ($)', marker='o')
plt.plot(monthly_summary['Month'], monthly_summary['Total Applications'], label='Total Applications', marker='x', linestyle='--')
plt.xlabel('Month')
plt.ylabel('Amount / Count')
plt.title('Average Amounts and Total Applications by Month')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
