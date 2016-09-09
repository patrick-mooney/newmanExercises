from numpy import sqrt

a,b,c = input("Gimme a,b,c: ")
xp = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
xm = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
print(xp, xm)

xm2 = (2*c) / (-b - sqrt(b**2 - 4*a*c))
xp2 = (2*c) / (-b + sqrt(b**2 - 4*a*c))
print(xp2,xm2)