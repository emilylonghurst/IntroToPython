import math

y = 1
x = 0.5
theta = 80 * (math.pi/180)
g = 9.81
v = 44

print(y + (x*math.tan(theta)) - (g*(x**2))/(2*(v*math.cos(theta))**2))

x = float(input("Please enter a value: "))
y = float(input("Please enter a value: "))

print(x+y)
