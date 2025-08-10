import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(courses)
    result= (
        df.groupby("class")["student"].nunique().reset_index().query("student>=5")[["class"]]
    )
    return result
    