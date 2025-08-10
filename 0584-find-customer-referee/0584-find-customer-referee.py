import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(customer)
    result= (
        df.query("referee_id !=2 or referee_id.isnull()")[["name"]]
    )
    return result