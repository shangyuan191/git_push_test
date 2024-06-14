a=int(input("input the force:"))
b=int(input("input the mass of m1:"))
c=int(input("input the distance:"))
G=6.67*10**-11
d=(a*(c*c))/(G*b)
e=d*2997924588**2
print("Input the force:"+" "+str(a))
print("Input the mass of m1:"+" "+str(b))
print("Input the distance:"+" "+str(c))
print("The mass of m2="+" "+str(d))
print("The energy of m2="+" "+str(e))
