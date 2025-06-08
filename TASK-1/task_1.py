#!/usr/bin/env python
# coding: utf-8

# TASK-1 : Calculate the number of applications, number of approved,
# and the number of used applications and visualize the trend over the submission date.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the applications data (already cleaned version)
df = pd.read_csv('path/applications.csv')

# Let’s quickly check the data types of each column
print(df.dtypes)

# Looks like 'submit_date' is a string — we'll need to convert it to a datetime format
type(df['submit_date'][0])

# Convert 'submit_date' into proper datetime format so we can work with time-based trends
df['submit_date'] = pd.to_datetime(df['submit_date'])
type(df['submit_date'][0])

# Preview the first few rows just to confirm everything looks good
df.head(5)

# Drop the unnecessary 'Unnamed: 0' column that came in from the CSV export
df.drop(columns=['Unnamed: 0'], inplace=True)
df.head(5)

# Make sure any blank values in key numeric columns are treated as actual missing data (NaN)
df['dollars_used'].replace('', pd.NA, inplace=True)
df['approved_amount'].replace('', pd.NA, inplace=True)

# Lets start the Visualization

# We'll set 'submit_date' as the index so we can analyze trends over time
df.set_index('submit_date', inplace=True)


# -------------------
# PLOT 1  Funnel Summary (All Time)
#------------------


# Total number of applications in the dataset
total_applications = df['application_id'].nunique()

# Total number of approvals
approved_applications = df[df['approved'] == True]['application_id'].nunique()

# Total number of applications where the customer actually used the funds
used_applications = df[df['dollars_used'].notna()]['application_id'].nunique()

funnel_data = pd.DataFrame({
    'Stage': ['Applied', 'Approved', 'Used'],
    'Count': [total_applications, approved_applications, used_applications]
})

# VISUALIZING THE FUNNEL
plt.figure(figsize=(8, 5))
sns.barplot(data=funnel_data, x='Stage', y='Count', palette='viridis')

plt.title('Application Funnel at Snap Finance')
plt.ylabel('Number of Applications')
plt.xlabel('Funnel Stage')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# -------------------
# PLOT 2 - Plotting Monthly
#------------------

# Convert to datetime, just making sure again
df['submit_date'] = pd.to_datetime(df['submit_date'])

# Set datetime as index
df = df.set_index('submit_date')  # Important: assign it back!

# Resample monthly and count
monthly_summary = df.resample('M').agg({
    'application_id': 'count',
    'approved': lambda x: (x == True).sum(),
    'dollars_used': lambda x: x.notna().sum()
})

# Rename columns for better understanding
monthly_summary.columns = ['Total Applications', 'Approved Applications', 'Used Applications']

# Plot it
monthly_summary.plot(title="Monthly Application Trends", figsize=(12, 6), marker='o')
plt.ylabel("Count")
plt.xlabel("Month")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
