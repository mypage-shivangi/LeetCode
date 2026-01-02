import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    managers = (
        employee
        .groupby('managerId')
        .size()
        .reset_index(name='cnt')
        .query('cnt >= 5')
    )

    return (
        employee
        .merge(managers, left_on='id', right_on='managerId')
        [['name']]
    )