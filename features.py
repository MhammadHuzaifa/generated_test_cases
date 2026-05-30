# features_vulnerable.py
import numpy as np

def add_features(df):
    feature_code = "df['rooms_per_household'] = df['total_rooms'] / df['households']"
    exec(feature_code)
    df['bedroom_ratio'] = df['total_bedrooms'] / df['total_rooms']
    return df