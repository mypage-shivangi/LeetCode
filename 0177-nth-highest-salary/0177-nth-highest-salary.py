import pandas as pd
import numpy as np
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    if N >0 and N<= len(distinct_salaries):
        result = distinct_salaries.iloc[N-1]
    else:
        result = np.nan
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})