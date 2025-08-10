import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    #df=pd.DataFrame(world)
    mask = (world["area"] >=3000000) | (world["population"] >=25000000)
    return world.loc[mask,["name","population","area"]]