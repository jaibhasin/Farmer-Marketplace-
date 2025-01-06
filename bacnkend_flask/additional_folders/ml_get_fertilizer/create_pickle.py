
import pandas as pd
import pickle

def create_pickle(csv_path, pickle_path):
    data = pd.read_csv(csv_path)
    with open(pickle_path, 'wb') as f:
        pickle.dump(data, f)

if __name__ == "__main__":
    csv_path = 'FertilizerData.csv'
    pickle_path = 'fertilizer_data.pkl'
    create_pickle(csv_path, pickle_path)