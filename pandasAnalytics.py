#pandas analytics
import pandas as pd

df = pd.read_csv('data_jobs.csv')

# shows the columns and what they look like...
print(df.info())

#shows a lot of aggrigrates
print(df.describe())

#get min
print(df['salary_year_avg'].min())

#get index of min
min_salary = df['salary_year_avg'].idxmin()

print(df['job_title_short'].value_counts())


##########################################
# GROUP BY
##########################################
# similar to how the GROUP BY works in SQL
print('GROUP BY DEMO')
print(df.groupby(['job_title_short', 'job_country'])['salary_year_avg'].min())


# how to use aggrigates
print(df.groupby('job_title_short')['salary_year_avg'].agg(['median','min','max','count']).sort_values('median' , ascending=False))

