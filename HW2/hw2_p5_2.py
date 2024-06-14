a=list(input("Enter a string: "))
b=[]
i=0
while(i<len(a)):
  j=i+1
  while(j<=len(a)):
    s=a[i:j]
    if(s==s[::-1]):
      b.append(s)
    j+=1
  i=i+1  
print("Longest palindrome substring is: "+"".join(max(b,key=len)))
print("Length is: "+str(len(max(b,key=len))))
    
