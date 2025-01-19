#matplotlibGenDemo

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data_jobs.csv')

df.info()

#get job counts
job_salary = df.groupby('job_title_short')['salary_year_avg'].median().sort_values()
print(job_salary)

# Format salary values with $ and k
formatted_salaries = [f"${int(salary // 1000)}k" for salary in job_salary.values]

# Plot bar chart with formatted labels
plt.barh(job_salary.index, job_salary.values)

# Add labels to the bars
for i, value in enumerate(job_salary.values):
    plt.text(value, i, formatted_salaries[i], va='center')

# Add titles and labels
plt.xlabel('Median Salary')
plt.ylabel('Job Title')
plt.title('Median Salary by Job Title')
plt.tight_layout()

# Show plot
plt.show()