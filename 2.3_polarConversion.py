from math import cos, atan, pi

x, y = float(input("Gimme x:")), float(input("Gimme y:"))
s = y/x
theta = atan(s)
r = x / cos(theta)
theta = theta*180/pi
print("r:", r, "\nTheta:", theta)