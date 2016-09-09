import matplotlib.pyplot as plt
from pylab import imshow, show, gray, hot
from numpy import sin, cos, pi, linspace, zeros, sqrt
 
def J(m, x):
    N = 10
    a = 0.
    b = pi
    h = (b-a)/N
    sOdd, sEven = 0., 0.
 
    s = f(m, x, a) + f(m, x, b)
    for k in range(1, N, 2):
        sOdd += f(m, x, a+k*h)
    sOdd *= 4
 
    for k in range(2, N, 2):
        sEven += f(m, x, a+k*h)
    sEven *= 2
 
    s += sOdd + sEven
    s *= h/3.
 
    return s / pi
 
 
def f(m, x, theta):
    return cos(m*theta - x*sin(theta))
 
#part b)
length = 500
wavelength = 500.e-9
m = 1
k = 2.*pi/wavelength
I = zeros([length,length], float)
for i in range(length):
    for j in range(length):
        r = sqrt( (i-(length/2))**2 + (j-(length/2))**2 ) * 1e-8
        if k*r < 1e-6:
            I[i,j] = .25
        else:
            I[i,j] = (J(m,k*r) / (k*r))**2
imshow(I, vmax = 0.01)
#gray()
hot()
show()
 
 
#part a)
#xPoints = linspace(0,20,1000)
#for m in range(3):
#   yPoints = []
#
#   for x in xPoints:
#       yPoints.append( J(m,x) )
#
#   if m == 0:
#       plt.plot(xPoints, yPoints, "b-")
#   elif m == 1:
#       plt.plot(xPoints, yPoints, "r-")
#   else :
#       plt.plot(xPoints, yPoints, "g-")
#plt.show()