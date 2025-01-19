#matplotlibP1

###############################
#Line Chart
###############################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data_jobs.csv')

#convert from string to date
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)
df['job_posted_month'] = df['job_posted_date'].dt.month

date_counts = df.job_posted_date.value_counts()
date_counts = date_counts.sort_index()

month_counts = df.job_posted_month.value_counts()
month_counts = month_counts.sort_index()

plt.plot(month_counts.index , month_counts.values)
plt.show()


