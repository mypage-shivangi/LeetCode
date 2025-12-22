import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rank']=employee['salary'].rank(method='dense',ascending=False)
    result=employee.loc[employee['rank']==2,['salary']]
    result=result.rename(columns={'salary':'SecondHighestSalary'})
    if result.empty:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    return result