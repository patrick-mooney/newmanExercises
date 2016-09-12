from numpy import sin, sqrt, abs, array, pi
import time
def f(x):
	#return sin(sqrt(100 * x))**2
	return 1/(sqrt(1-9*sin(x)**2))

N = 1
a = 0.
b = pi/2.
h = (b-a) / N
acc = 1.0e-13
err = 1.
s, si, s2f = 0., 0., 0.
R = []
i, j = 0, 0

si = .5*(f(a) + f(b))*h
R.append([si])
N*=2
h = (b-a)/N

start = time.time()

while abs(err) > acc:
	i += 1
	sf = 0.
	for k in range(1,N,2):
		sf += f(a+k*h)
	sf *= h
	sf += .5*si

	R.append([sf])
	for j in range(0,i):
		s = R[i][j] + (1 / (4**(j+1) - 1)) * (R[i][j] - R[i-1][j])
		(R[i]).append(s)

	err = (1 / (4**(i+1) - 1)) * (R[i][i-1] - R[i-1][i-1])
	N *= 2
	h = (b-a) / N
	si = sf
	#print(sf)

end = time.time() - start
print (R[i][i])
print (N/2)
print (err)
print (end)
print ("\n")
#print (R)
