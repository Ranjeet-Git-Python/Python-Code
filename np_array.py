import numpy as np

sales = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(sales)
value = sales[1,2]
print("value at row 1 and column2:", value)
slice_part = sales[0:3,1:3]
print("slice sub array row 0 to 2 and column 1 to 2:\n",slice_part)