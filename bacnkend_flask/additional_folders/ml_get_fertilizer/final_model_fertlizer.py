import pickle
from dict1 import fertilizer_dic
from markupsafe import Markup

def load_fertilizer_data(pickle_path):
    with open(pickle_path, 'rb') as f:
        return pickle.load(f)

def recommend_fertilizer(N, P, K, crop, data):
    crop_data = data[data['Crop'] == crop]
    
    if crop_data.empty:
        print(f"No data available for crop: {crop}")
        return
    
    n = crop_data['N'].iloc[0] - N
    p = crop_data['P'].iloc[0] - P
    k = crop_data['K'].iloc[0] - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]
    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = "Plow"
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = "Klow"

    response = Markup(str(fertilizer_dic[key]))
    print(response)

def user_input(N,P,K,crop):
    pickle_path = 'fertilizer_data.pkl'
    data = load_fertilizer_data(pickle_path)
    

    recommend_fertilizer(N, P, K, crop, data)


user_input(24, 33 , 43,"rice")