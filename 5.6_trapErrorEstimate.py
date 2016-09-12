def f(x):
	return x**4 - 2*x + 1

N1, N2 = 10, 20
a = 0.
b = 2.
h1, h2 = (b-a)/N1, (b-a)/N2
s1 = .5*(f(a) + f(b))
s2 = .5*(f(a) + f(b))

for k in range(1,N1):
	s1+= f(a+k*h1)
s1 *= h1

for k in range(1,N2):
	s2 += f(a+k*h2)
s2 *= h2

err = (s2-s1) / 3.

print (s1)
print (s2)
print (err)
print(s2 + err)