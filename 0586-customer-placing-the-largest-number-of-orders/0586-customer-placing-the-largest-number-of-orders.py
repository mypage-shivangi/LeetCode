import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orderscnt= (
        orders
        .groupby('customer_number')['order_number']
        .size()
        .reset_index(name='cnt')
    )
    return orderscnt.loc[
        orderscnt['cnt']==orderscnt['cnt'].max(),
        ['customer_number']

    ]