import pandas as pd
import numpy as np

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    #auth=views["author_id"].to_numpy()
    #v_id=views["viewer_id"].to_numpy()
    #mask=(auth==v_id)
    #return pd.DataFrame({"id":np.sort(views.loc[mask,"author_id"].unique())})
    df=views[views['author_id']==views['viewer_id']]
    return df[['author_id']] \
        .drop_duplicates() \
        .rename(columns={'author_id': 'id'}) \
        .sort_values('id', ascending=True)
