from numpy import loadtxt
import matplotlib.pyplot as plt
v = loadtxt("velocities.txt", float)

N = 100
a = 0.
b = 100.
h = (b-a)/N
s = .5*v[0,1]
x = []
x.append(s)
for k in range(1,100):
	s+= v[k,1]
	x.append(s)
s += .5*v[100,1]
x.append(s)
print s
plt.plot(range(101),v[:,1],range(101),x)
plt.show()
