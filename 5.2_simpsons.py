def f(x):
	return x**4 - 2*x + 1

N = 1000
a = 0.
b = 2.
h = (b-a)/N
sOdd, sEven = 0., 0.

s = f(a) + f(b)
for k in range(1, N, 2):
	sOdd += f(a+k*h)
sOdd *= 4

for k in range(2, N, 2):
	sEven += f(a+k*h)
sEven *= 2

s += sOdd + sEven
s *= h/3.

print (s)
