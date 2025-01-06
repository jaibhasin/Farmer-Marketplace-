import pandas as pd
from dict1 import fertilizer_dic
from markupsafe import Markup

# Load the fertilizer data
fertilizer_data_path = 'FertilizerData.csv'
merge_fert = pd.read_csv(fertilizer_data_path)

def recommend_fertilizer(N, P, K, crop):
    # Filter the fertilizer data for the specific crop
    crop_data = merge_fert[merge_fert['Crop'] == crop]
    
    if crop_data.empty:
        print(f"No data available for crop: {crop}")
        return
    
    # Calculate the difference between user input and recommended values
    N_diff = crop_data['N'].iloc[0] - N
    P_diff = crop_data['P'].iloc[0] - P
    K_diff = crop_data['K'].iloc[0] - K
    
    print(f"Recommended adjustments for {crop}:")
    print(f"Nitrogen (N): {N_diff}")
    print(f"Phosphorus (P): {P_diff}")
    print(f"Potassium (K): {K_diff}")
    
    # Provide a list of sentences based on the differences
    recommendations = []
    if N_diff > 0:
        recommendations.append(f"To increase Nitrogen (N) by {N_diff}, consider using a Nitrogen-rich fertilizer.")
    if P_diff > 0:
        recommendations.append(f"To increase Phosphorus (P) by {P_diff}, consider using a Phosphorus-rich fertilizer.")
    if K_diff > 0:
        recommendations.append(f"To increase Potassium (K) by {K_diff}, consider using a Potassium-rich fertilizer.")
    
    if recommendations:
        print("Recommended actions:")
        for recommendation in recommendations:
            print(f"- {recommendation}")
    else:
        print("No additional fertilizers needed.")
    
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

# Example usage
if __name__ == "__main__":
    N = int(input("Enter the value of Nitrogen (N): "))
    P = int(input("Enter the value of Phosphorus (P): "))
    K = int(input("Enter the value of Potassium (K): "))
    crop = input("Enter the crop you want to grow: ")

    recommend_fertilizer(N, P, K, crop)