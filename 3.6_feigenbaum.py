from pylab import scatter, show,plot
from numpy import linspace,empty
import matplotlib.pyplot as plt

r = linspace(1,4,10001)
x = empty([10001],float)
x[:] = .5
j = 0
x2,r2 = [],[]
for n in r:
	print(n)
	for i in range(1000):
		x[j] = n*x[j]*(1-x[j])
	for i in range(250):
		x[j] = n*x[j]*(1-x[j])
		#plt.scatter(n,x[j],1)
		x2.append(x[j])
		r2.append(n)
	j+=1
plt.scatter(r2,x2,s=1,alpha = .2)	
#plot(r,x,"k.")
plt.show()