import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

x = []
y = []

print("Enter x and y values:")

for i in range(n):
    xi = float(input(f"x{i+1}: "))
    yi = float(input(f"y{i+1}: "))
    x.append(xi)
    y.append(yi)

plt.plot(x, y, marker='o')
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()