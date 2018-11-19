import os
import pandas as pd
import matplotlib.pyplot as plt

employee_info_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/data_employee/employee_info.csv'

employee_edu_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/data_employee/employee_edu.csv'

output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

employee_info = pd.read_csv(employee_info_path)
employee_edu = pd.read_csv(employee_edu_path)

merged_df = pd.merge(employee_info,employee_edu,how='inner',on='EmployeeNumber')

mean_salary_ser = merged_df.groupby('EducationField')['MonthlyIncome'].mean()
mean_salary_ser.sort_values(ascending=False,inplace=True)

plt.figure(figsize=(10, 8))
mean_salary_ser.plot(kind='bar',rot=45)
plt.ylabel('Monthly average salary')
plt.show()


