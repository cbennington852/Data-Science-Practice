#pivotTables

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data_jobs.csv')

#convert from string to date
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

df.info()


print(df.pivot_table(
    values='salary_year_avg', 
    index='job_country', 
    columns='job_title_short', 
    aggfunc='size')
)