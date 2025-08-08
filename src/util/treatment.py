import pandas as pd

def initial_information_dataset(df: pd.DataFrame):
    result = {}
    result["num_rows"] = df.shape[0]
    result["num_columns"] = df.shape[1]
    result_col = {}
    for c in df.columns:
        result_col[c] = {"type":df[c].dtype,
                     "non_null":df[c].dropna().shape[0],
                     "null": df.shape[0] - df[c].dropna().shape[0],
                     "non_duplicates":df[c].drop_duplicates().shape[0]}
    result["columns"] = result_col
    return result