import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    valid=users[users['mail'].str.match(pattern)]
    return valid
    