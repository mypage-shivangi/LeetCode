import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(candidates,rounds,on='interview_id',how='left')
    result = (
        df
        .groupby('candidate_id', as_index=False)
        .agg(
            score=('score', 'sum'),
            years_of_exp=('years_of_exp', 'max')
        )
        .query('score > 15 and years_of_exp >= 2')
        [['candidate_id']]
    )

    return result