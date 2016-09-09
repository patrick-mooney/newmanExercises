from numpy import sqrt
L=1000000
s = 100
M = 0.0
for i in range(0,s):
	for j in range(0,s):
		for k in range(0,s):
			if (i+j+k)%2 :
				M += -1/sqrt(i**2+j**2+k**2+1)
			else:
				M += 1/sqrt(i**2+j**2+k**2+1)
	
print(M)
		