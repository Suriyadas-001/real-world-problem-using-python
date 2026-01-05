# 1. Employee Management System
# Create a Python program that uses a nested dictionary to store details of multiple employees, where each employee record contains the employee’s name, department, age, salary, and performance rating on a scale of 1 to 5. Write separate functions to process this data such that the salary of each employee is increased based on performance, giving a 20 percent salary hike to employees whose rating is 4 or above, a 10 percent hike to employees with a rating of 3, and no hike to employees whose rating is below 3. The program should also print employee details department-wise, identify and display the highest-paid employee, and remove all employees whose age is greater than 60 from the records.

# data for details of employees
emp_data = {
    'emp_1' : {
        'name' : 'Indrajit Giri',
        'dept' : 'DBA',
        'age' : 23,
        'salary' : 45000,
        'performance_rate' : 3.9
    },
    'emp_2' : {
        'name' : 'Siraj Besra',
        'dept' : 'IT',
        'age' : 21,
        'salary' : 35000,
        'performance_rate' : 3.5
    },
    'emp_3' : {
        'name' : 'Subhajit Maity',
        'dept' : 'Finance',
        'age' : 22,
        'salary' : 30000,
        'performance_rate' : 2.9
    },
    'emp_4' : {
        'name' : 'Sujoy Das',
        'dept' : 'HR',
        'age' : 20,
        'salary' : 55000,
        'performance_rate' : 4.2
    },
    'emp_5' : {
        'name' : 'Ankan Patra',
        'dept' : 'IT',
        'age' : 22,
        'salary' : 42000,
        'performance_rate' : 4
    }
}

# function for increased salary
def increased_salary():
    for emp_id,emp_details in emp_data.items():
        # print(emp_details['performance_rate'])
        if emp_details['performance_rate'] >=4:
            emp_details['salary'] += (emp_details['salary']*20)/100
        elif emp_details['performance_rate'] <4 and emp_details['performance_rate'] >= 3:
            emp_details['salary'] += (emp_details['salary']*10)/100
print(emp_data)
increased_salary()
print(emp_data)
