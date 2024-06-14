a=float(input("Please input a Richter scale value: "))#輸入芮氏規模 
e=10**(1.5*a+4.8)#計算能量
j=e#單位是焦耳
t=e/(4.184*(10**9))#計算該能量等於多少炸藥
n=e/2930200#計算該能量等於多少份營養午餐
print("Ritcher scale value: "+str(a))#印出芮氏規模
print("Equivalence in Joules: "+str(j))#印出多少焦耳
print("Equivalence in tons of TNT : "+str(t))#印出多少炸藥
print("Equivalence in the number of nutritious lunches: "+str(n))#印出多少份營養午餐
