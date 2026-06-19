import numpy as np

data = np.loadtxt("amazon_data.csv", delimiter="," , skiprows=1, usecols=(1,2,3))
print(data)
sales = data[:,0]
customers = data[:,1]
orders = data[:,2]
print(sales)
print(customers)
print(orders)
total_sales = np.sum(sales)
avg_sales = np.mean(sales)
max_sales = np.max(sales)
min_sales = np.min(sales)

total_customer = np.sum(customers)
avg_customer = np.mean(customers)

total_orders = np.sum(orders)
avg_orders = np.mean(orders)

print("Yearly data analysis:")
print("-------------------------")
print(f"Total sales:, ${total_sales:,.2f}")
print(f"Average sales:, ${avg_sales:.2f}")
print(f"Highest sales:, ${max_sales:.2f}")
print(f"Lowest sales:, ${min_sales:.2f}")
print()
print(f"Total customers registered: {total_customer:,.2f}")
print(f"Average customers : {avg_customer:.2f}")


