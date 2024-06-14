hb1=int(input("Input the height of the 1st ball: "))
mb1=int(input("Input the mass of the 1st ball: "))
mb2=int(input("Input the mass of the 2nd ball: "))
u=mb1*9.8*hb1
u1=(2*u/mb1)**0.5
v2=((mb1*2)/(mb1+mb2))*u1
print("Input the height of the 1st ball: "+str(hb1))
print("Input the mass of the 1st ball: "+str(mb1))
print("Input the mass of the 2nd ball: "+str(mb2))
print("The velocity of the 1st ball after slide: "+str(u1)+"m/s")
print("The velocity of the 2nd ball after collision: "+str(v2)+ "m/s")