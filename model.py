# ---------------------------------------
# CODTECH Internship - Task 4
# Optimization Model using Linear Programming Concept
# Business Problem: Profit Maximization
# ---------------------------------------

import matplotlib.pyplot as plt

# Profit per unit of each product
profit_A = 40   # Profit for Product A
profit_B = 30   # Profit for Product B

# Constraints:
# 2A + B <= 100
# A + 2B <= 80
# A >= 0, B >= 0

best_profit = 0
best_A = 0
best_B = 0

# Brute-force approach to find optimal solution
for A in range(0, 101):
    for B in range(0, 101):
        if (2 * A + B <= 100) and (A + 2 * B <= 80):
            total_profit = profit_A * A + profit_B * B
            if total_profit > best_profit:
                best_profit = total_profit
                best_A = A
                best_B = B

# Display results
print("Optimal Solution:")
print("Product A Units =", best_A)
print("Product B Units =", best_B)
print("Maximum Profit =", best_profit)

# Visualization of results
products = ["Product A", "Product B"]
values = [best_A, best_B]

plt.figure()
plt.bar(products, values)
plt.title("Optimal Production Plan")
plt.xlabel("Products")
plt.ylabel("Units Produced")

# Save output image
plt.savefig("optimization_output.png")
plt.show()
