def f(x):
	return x*(x-1)

h = 1e-2
x=1

print (f(x+h) - f(x)) / h
