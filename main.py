from seaborn import load_dataset
import numpy as np
import pandas as pd
from collections import Counter
#a function to find distance between two points using Euclidean distance
def Distance(Point1, Point2):
    return np.linalg.norm(Point1 - Point2)
#a function I found online
def most_common(DataSet):
    return Counter(DataSet).most_common(1)[0][0]

k_val = 3 #k-value for the k-nearest-neighbours
data = load_dataset("penguins")
data.drop(columns=["island", "sex", "bill_length_mm", "bill_depth_mm"])
DatSpecies = data.pop("species").dropna()
DatIndices = data.index
unknown_penguin = pd.DataFrame([[191.0, 3900]], columns=["flipper_length_mm", "body_mass_g"])


distances = [Distance(data.iloc[row], unknown_penguin.iloc[0]) for row in DatIndices] #finds the distance between the given point and all the others
DistIndices = np.argsort(distances)[:k_val] #sorts the distances by index to get indices of shortest distances
#We are interested in first (k) indices

var = DatSpecies.iloc[DistIndices]

mostcommon = most_common(var)
print(f"The species of Unknown penguin is {mostcommon}")
