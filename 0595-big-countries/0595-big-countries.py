import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(world)
    result = df.loc[
        (df["area"] >=3000000) | (df["population"] >=25000000),
        ["name","population","area"]]
    return result