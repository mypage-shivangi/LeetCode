import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df=(products['low_fats']=='Y') & (products['recyclable']=='Y')
    return products.loc[df,['product_id']]
    