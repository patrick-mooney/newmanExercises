G = 6.67e-11
M = 5.97e24
R = 6371000
pi = 3.14159
T = float( input("gimme the time: ") )

h = ( (G*M*T**2)/(4*pi**2) )**(1/3) - R

print(h)