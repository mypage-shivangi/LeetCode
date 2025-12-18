import pandas as pd
import numpy as np
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    result=employee.loc[employee['rank']==N,['salary']]
    if result.empty:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    return pd.DataFrame({f'getNthHighestSalary({N})': result.iloc[0]})