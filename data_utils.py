# data_utils_vulnerable.py
import pandas as pd
import pickle
from repo_make.config import DATA_PATH

def load_data():
    df = pd.read_csv(DATA_PATH)
    if 'formula' in df.columns:
        df['result'] = df['formula'].apply(lambda x: eval(x))
    return df

def load_model_unsafe(path):
    with open(path, 'rb') as f:
        return pickle.load(f)