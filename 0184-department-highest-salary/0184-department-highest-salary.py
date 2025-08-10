import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if employee.empty:
       return pd.DataFrame(columns=['Department', 'Employee', 'salary'])
    # Calculate rank (dense_rank equivalent) of salaries within each department
    employee['dense_rank'] = employee.groupby('departmentId')['salary'] \
                                    .rank(method='dense', ascending=False)
    
    # Filter to only highest salary (rank = 1)
    top_salaries = employee[employee['dense_rank'] == 1].copy()
    
    # Join with department on departmentId
    result = pd.merge(department, top_salaries, left_on='id', right_on='departmentId', how='left')
    
    # Select columns you want to return, e.g. department name, employee name, salary
    result= result[['name_x', 'name_y', 'salary']].rename(columns={
        'name_x': 'Department',
        'name_y': 'Employee'
    })
    return result
