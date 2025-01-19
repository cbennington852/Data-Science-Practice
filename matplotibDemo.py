#matplot lib demo
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data_jobs.csv')

#convert from string to date
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

x = np.arange(0,5,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()



