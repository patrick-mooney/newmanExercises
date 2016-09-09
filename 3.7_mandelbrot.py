from pylab import imshow, show, gray, colorbar
from numpy import empty, linspace, abs, real, zeros
from math import isnan
N = 1000
c = zeros([N,N], int)
z = 0+0j
v = 0
h = 0
l = 0
for y in linspace(-2,2,N):
	for x in linspace(-2,2,N):
		for i in range(100):
			#print(z)
			z = complex(z**2) + complex(x,y)
			l+=1
			if abs(z) > 2 or isnan(real(z)):
				break
			#print(complex(z**2) + complex(x,y))
		#print(complex(x,y))	
		#if abs(z) > 2 or isnan(real(z)):
		#	c[v,h] = 1
		#else:
		#	c[v,h] = 0
		c[v,h] = l
		z = 0+0j
		h += 1
		l=0
	v += 1
	h = 0
		

imshow(c, origin = "lower")

colorbar()
show()