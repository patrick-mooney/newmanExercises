from numpy import sqrt

def fxk(h, k):
	return -1 + h*k

def fyk(h,k):
	return sqrt(1 - fxk(h, k)**2)
	
N = 50000000
h = 2./N
I = 0
for k in range(1,N):
	I += fyk(h, k)
print I*h

