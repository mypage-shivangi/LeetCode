import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    # Step 1: Rank salaries
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    
    # Step 2: Filter second highest salary
    result = employee.loc[employee['rank'] == 2, 'salary']
    
    # Step 3: Handle missing case
    if result.empty:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    # Step 4: Return unique value
    return pd.DataFrame({'SecondHighestSalary': [result.iloc[0]]})
