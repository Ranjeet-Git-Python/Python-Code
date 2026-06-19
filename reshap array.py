import numpy as np

data = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshaped = data.reshape(3,4)
print("Reshaped array:\n", reshaped)

more_data = np.array([
   [13,14,15,16],
   [17,18,19,20],
    [21,22,23,24]
])
combined_v = np.vstack((reshaped,more_data))
combined_h = np.hstack((reshaped,more_data))
print("vertically combined array:\n", combined_v)
print("horizontally combined array:\n",combined_h)
