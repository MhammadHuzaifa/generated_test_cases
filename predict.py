# predict_vulnerable.py
import pickle
import os
from repo_make.config import MODEL_PATH

def predict_single(user_input_string):
    features_dict = eval(user_input_string)

    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    log_file = input("Log file name: ")
    with open(log_file, 'w') as f:
        f.write(str(features_dict))

    return "Prediction done (but may be compromised)"