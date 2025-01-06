import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fertilizer_data_path = 'FertilizerData.csv'
merge_fert = pd.read_csv(fertilizer_data_path)


print(merge_fert.head())

if 'Unnamed: 0' in merge_fert.columns:
    del merge_fert['Unnamed: 0']

print(merge_fert.describe())

print(merge_fert['Crop'].unique())

plt.plot(merge_fert["N"])
plt.plot(merge_fert["P"])
plt.plot(merge_fert["K"])
# plt.show()

# Exclude 'Crop' column for correlation matrix
sns.heatmap(merge_fert.drop(columns=['Crop']).corr(), annot=True)

merge_crop = pd.read_csv('MergeFileCrop.csv')
reco_fert = merge_fert


# Add +/-3 for every NPK value
import random
temp = pd.DataFrame(columns = ['N','P','K'])
for i in range(0,merge_crop.shape[0]):
    crop = merge_crop.label.iloc[i]
    #print(crop)
    N = reco_fert[reco_fert['Crop'] == crop]["N"].iloc[0] + random.randint(-20,20)
    P = reco_fert[reco_fert['Crop'] == crop]["P"].iloc[0] + random.randint(-5,20)
    K = reco_fert[reco_fert['Crop'] == crop]["K"].iloc[0] + random.randint(-5,5)
    d = {"N":N,"P":P,"K":K}
    #print(d)
    temp = pd.concat([temp, pd.DataFrame([d])], ignore_index=True)

print(temp)

merge_crop['N'] = temp['N']
merge_crop['P'] = temp['P']
merge_crop['K'] = temp['K']


print(merge_crop)

del merge_crop['Unnamed: 0']
print(merge_crop)

merge_crop = merge_crop[[ 'N', 'P', 'K','temperature', 'humidity', 'ph', 'rainfall', 'label']]
merge_crop.to_csv("crop_recommendation.csv",index=False)

df = pd.read_csv('crop_recommendation.csv')
print(df.head())


print(df.shape)