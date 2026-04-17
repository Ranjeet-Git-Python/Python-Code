n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     leading = " " * ((n - i) * 2)
#     between = " " * ((i - 1) * 2)
#     print(leading + between.join([str(i)] * i))

# 2nd method
for i in range(1, n):
    print(((10 ** (i)) // 9) *  i)