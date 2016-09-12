from numpy import sin, sqrt, abs
import time

# comparing times for adaptive trap with no dynamic programming
# with the method using dynaprog 4 fun

def f(x):
	return sin(sqrt(100*x))**2

N = 1
acc = 1.0e-12
a = 0.
b = 1.
h = (b-a)/N
si, sf = 0., 0.
err = 1.

start = time.time()

while abs(err) > acc:
	sf = .5 * (f(a) + f(b))
	for k in range(1,N):
		sf += f(a+k*h)
	sf *= h

	err = (sf - si) / 3.
	N *= 2
	h = (b-a) / N
	si = sf

end1 = time.time() - start
print (N/2)
print (sf)
print (acc)
print (err)

############################################################################
# dynamic method
N = 1
acc = 1.0e-12
a = 0.
b = 1.
h = (b-a)/N
si, sf = 0., 0.
err = 1.

start = time.time()

si = .5*(f(a)+f(b))*h
N*=2
h = (b-a)/N
while abs(err) > acc:
	sf = 0.
	for k in range(1,N,2):
		sf += f(a+k*h)
	sf *= h
	sf += .5*si

	err = (sf - si) / 3.
	N *= 2
	h = (b-a) / N
	si = sf

end2 = time.time() - start

print ("\n")
print (N/2)
print (sf)
print (acc)
print (err)
print("\n")
print(end1)
print(end2)