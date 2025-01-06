import pickle
from myproject.dict1 import fertilizer_dic
from markupsafe import Markup

def load_fertilizer_data(pickle_path):
    with open(pickle_path, 'rb') as f:
        return pickle.load(f)

def recommend_fertilizer(N, P, K, crop, data):
    crop_data = data[data['Crop'] == crop]

    if crop_data.empty:
        return {"error": f"No data available for crop: {crop}"}

    n = int(crop_data['N'].iloc[0]) - int(N)
    p = int(crop_data['P'].iloc[0]) - int(P)
    k = int(crop_data['K'].iloc[0]) - int(K)
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
    return response

def user_input(N,P,K,crop):
    pickle_path = './myproject/pkl_files/fertilizer_data.pkl'
    data = load_fertilizer_data(pickle_path)


    return recommend_fertilizer(N, P, K, crop, data)
