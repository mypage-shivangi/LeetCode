def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if employee.empty:
        return pd.DataFrame(columns=['Department', 'Employee', 'salary'])
    
    employee['dense_rank'] = employee.groupby('departmentId')['salary'] \
                                    .rank(method='dense', ascending=False)
    top_salaries = employee[employee['dense_rank'] == 1].copy()
    result = pd.merge(department[['id', 'name']], top_salaries, left_on='id', right_on='departmentId', how='inner')
    result = result[['name_x', 'name_y', 'salary']].rename(columns={
        'name_x': 'Department',
        'name_y': 'Employee'
    })
    return result.sort_values(by='Employee').reset_index(drop=True)
