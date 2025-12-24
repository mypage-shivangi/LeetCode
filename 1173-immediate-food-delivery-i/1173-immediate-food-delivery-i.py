import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate=delivery.loc[delivery['order_date'] == delivery['customer_pref_delivery_date']].shape[0]
    total=delivery.shape[0]
    immediate_percentage=round(immediate/total*100,2)
    return pd.DataFrame({'immediate_percentage':[immediate_percentage]})