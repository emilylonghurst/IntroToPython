import math

y = float(input("Please input the height of the barrel (m): "))
x = float(input("Please input the horizontal distance travelled (m): "))
theta = float(input("Please input the elevation angle (degrees): "))
thetaNew = theta * (math.pi/180)
g = 9.81
v = float(input("Please input the initial velocity (m/s): "))

print(y + (x*(math.tan(thetaNew))) - ((g*(x**2)) / (2*(v*((math.cos(thetaNew))**2)))))

x = float(input("Please enter a value: "))
y = float(input("Please enter a value: "))

print(x+y)
