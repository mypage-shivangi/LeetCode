import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    area = world["area"].to_numpy()
    pop = world["population"].to_numpy()
    mask = (area >= 3000000) | (pop >= 25000000)
    return world.loc[mask, ["name", "population", "area"]]