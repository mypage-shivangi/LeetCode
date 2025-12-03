import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = (
        ((employees['employee_id'] % 2 != 0) & (employees['name'].str[0] != 'M'))
        .astype(int)
        * employees['salary']
    )
    return employees[['employee_id','bonus']].sort_values('employee_id')
    