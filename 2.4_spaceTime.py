from math import sqrt

x, v = float(input("gimme x: ")), float(input("gimme v: "))
t = x/v
tp = t*(sqrt(1-v**2))
print("Time to observer on earth:", t, "\nTime to ship passenger:", tp)
