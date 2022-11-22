from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
scaler = MinMaxScaler(feature_range=(-1, 1))

print(scaler.transform(data[1]))
