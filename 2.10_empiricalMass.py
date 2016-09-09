from numpy import sqrt
A = input("wut is A: ")
Z = input("wut is Z: ")
a1 = 15.8
a2 = 18.3
a3 = 0.714
a4 = 23.2
if A%2 :
	a5 = 0.0;
elif Z%2 :
	a5 = -12.0
else :
	a5 = 12.0
	
B = (a1*A) - (a2*(A**(2.0/3.0))) - (a3*((Z**2)/(A**(1.0/3.0)))) - \
	 (a4*(((A-(2*Z))**2)/A)) + (a5/(sqrt(A)))

print(B)