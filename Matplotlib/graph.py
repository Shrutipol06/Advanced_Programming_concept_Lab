
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# 1. Line Graph
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 2. Bar Graph
plt.figure()
plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 3. Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 4. Pie Chart
plt.figure()
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# 5. Histogram
data = [10, 12, 15, 15, 18, 20, 22, 22, 25, 30]
plt.figure()
plt.hist(data, bins=5)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
