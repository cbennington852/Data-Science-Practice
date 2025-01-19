#The data part of learning
from datetime import datetime

data_science_jobs = [
    {'job_title': 'Data Engineer', 'job_skills': "['SQL', 'Python', 'Tableau']", 'job_date': '2024-11-15'},
    {'job_title': 'Data Scientist', 'job_skills': "['Python', 'Machine Learning', 'TensorFlow']", 'job_date': '2024-10-30'},
    {'job_title': 'Business Analyst', 'job_skills': "['Excel', 'SQL', 'Power BI']", 'job_date': '2024-09-20'},
    {'job_title': 'Machine Learning Engineer', 'job_skills': "['Python', 'Scikit-learn', 'Deep Learning']", 'job_date': '2024-12-05'},
    {'job_title': 'Data Analyst', 'job_skills': "['SQL', 'Tableau', 'R']", 'job_date': '2024-11-10'},
    {'job_title': 'AI Researcher', 'job_skills': "['Python', 'Natural Language Processing', 'PyTorch']", 'job_date': '2024-08-25'},
    {'job_title': 'Statistician', 'job_skills': "['R', 'Statistical Analysis', 'Data Visualization']", 'job_date': '2024-07-15'},
    {'job_title': 'Database Administrator', 'job_skills': "['SQL', 'Database Management', 'PostgreSQL']",'job_date': '2024-06-01'},
    {'job_title': 'Big Data Engineer', 'job_skills': "['Hadoop', 'Spark', 'Python']", 'job_date': '2024-12-20'},
    {'job_title': 'Data Architect', 'job_skills': "['Data Modeling', 'SQL', 'Cloud Computing']", 'job_date': '2024-11-01'}
]

test_date = data_science_jobs[0]['job_date']

print(datetime.now())

print(datetime.strptime(test_date , '%Y-%m-%d'))

import ast

for job in data_science_jobs:
    #make job time better
    job['job_date'] = datetime.strptime(job['job_date'], '%Y-%m-%d')
    #make the string into an array
    job['job_skills'] = ast.literal_eval(job['job_skills'])
    
#print(data_science_jobs)




#######################################
#Data stuff :: numpy
#######################################

import pandas as pd
import numpy as np
import random
import statistics 

salary_list = np.array([random.randint(50000,100000) for _ in range(1_000_000)])
print(salary_list)

#print(statistics.mean(salary_list))
print(salary_list.mean()) # this is faster , much faster



