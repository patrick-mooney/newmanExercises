from numpy import linspace, sin, cos, pi, exp
from pylab import plot, show

x, y = [], []

#part fuckin a
#n = linspace(0,2*pi,5)
#for theta in n:
#	x.append(2*cos(theta) + cos(2*theta))
#	y.append(2*sin(theta) - sin(2*theta))
	  
#plan b
#n = linspace(0,20*pi,1000)
#for theta in n:
#	r = theta**2
#	x.append(r*cos(theta))
#	y.append(r*sin(theta))
	
#part c
n = linspace(0,24*pi,10000)
for theta in n:
	r = exp(cos(theta)) - 2*cos(4*theta) + sin(theta/12.0)**5
	x.append(r*cos(theta))
	y.append(r*sin(theta))
plot(y,x)
show()