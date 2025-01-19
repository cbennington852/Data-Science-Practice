#matplotlibGenDemo
###############################
#bar Chart
###############################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data_jobs.csv')

#get job counts
job_counts = df.job_title_short.value_counts()
job_counts = job_counts.sort_values()
print(job_counts)


plt.barh(job_counts.index, job_counts.values)
plt.show()

#bar shows vertilce graph
plt.bar(job_counts.index, job_counts.values)
plt.title('Job counts by title')
plt.ylabel('count of job postings')
plt.xticks(rotation=45, ha='right')
plt.show()
