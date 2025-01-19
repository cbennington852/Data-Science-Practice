#pandas intro
import pandas as pd

df = pd.read_csv('data_jobs.csv')

# shows the columns and what they look like...
print(df.info())

#return first 5 rows
print(df.head(5))

#return last 5 rows
print(df.tail(5))

#only gets two collumns like --> SELECT job_title_short , job_location
print(df[['job_title_short','job_location']])

#collms 90-100 and rows 0-2
df.iloc[90:100, 0:2]

#tells us the info about the table ... the count of non-null values
#very very usefullll!!!!!
df.info()


#gets basic info .. count, mean,min, 25% ,50% ,75%
print(df.describe())

#retunrs all of rhe unique values
print(df.job_title_short.unique())

#only returns the ones with Data Analyst
print(df.job_title_short == 'Data Analyst')

#sets df to be only Data Analyst and sets salary 
df[(df.job_title_short == 'Data Analyst') | (df.salary_year_avg > 100000)]
print(df)


######################################################################
#Data Cleaning
######################################################################

#convert from string to date
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

#sorts the values
df.sort_values('job_posted_date', inplace=True)
print(df.job_posted_date)

