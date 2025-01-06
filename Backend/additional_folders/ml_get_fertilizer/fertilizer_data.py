
import pandas as pd
import pickle

def load_fertilizer_data(csv_path):
    return pd.read_csv(csv_path)

def save_fertilizer_data(data, pickle_path):
    with open(pickle_path, 'wb') as f:
        pickle.dump(data, f)

def load_fertilizer_data_from_pickle(pickle_path):
    with open(pickle_path, 'rb') as f:
        return pickle.load(f)