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

# The program should also print employee details department-wise
def details_of_emp_dept_wise():
    data = arrange_data_dept_wise()
    print("Details of Employees depertment wise\n")
    for dept in data:
        print(f"................{dept}.................\n")
        for emp_id,emp_details in data[dept]:
            print(f"Emp id {emp_id}")
            print(f"Emp name {emp_details['name']}")
            print(f"Emp dept {emp_details['dept']}")
            print(f"Emp age {emp_details['age']}")
            print(f"Emp salary {emp_details['salary']}")
            print(f"Emp performance_rate {emp_details['performance_rate']}\n")

# arrange the data depertment-wise
def arrange_data_dept_wise():
    emp_dept = {}
    for emp_id,emp_details in emp_data.items():
        dept = emp_details['dept']
        if dept not in emp_dept.keys():
            emp_dept[dept] = []
        emp_dept[dept].append((emp_id,emp_details))
    return emp_dept
# highest paid employee -this code is written by gpt
def highest_paid_emp():
    # Find the employee with the maximum salary
    highest_emp_id = max(emp_data, key=lambda eid: emp_data[eid]['salary'])
    highest_emp = emp_data[highest_emp_id]
    print("Highest Paid Employee Details:")
    print(f"Emp id: {highest_emp_id}")
    print(f"Emp name: {highest_emp['name']}")
    print(f"Emp dept: {highest_emp['dept']}")
    print(f"Emp age: {highest_emp['age']}")
    print(f"Emp salary: {highest_emp['salary']}")
    print(f"Emp performance_rate: {highest_emp['performance_rate']}\n")
    
if __name__=="__main__":
    # increased_salary()
    # details_of_emp_dept_wise()
    highest_paid_emp()
    