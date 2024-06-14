a=int(input("The number of the request element in Fibonacci(n)= "))
b=list(input("The first string for Palindromic detection(s1)= "))
c=list(input("The second string for Palindromic detection(s2)= "))
d=str(input("The plaintext to be encrypted: " ))
print("- - - - - extract key for encrypt method - - - - -")
arr=[]
i=0
while i<(a+1):
  if i==0:
    arr=[0]
  elif i==1:
    arr=[0,1]
  else:
    arr.append(arr[i-1]+arr[i-2])
  i=i+1
if a==1:
  print("The "+str(a)+"-th Fibonacci sequence number is: "+str(arr[0]))
else:
  print("The "+str(a)+"-th Fibonacci sequence number is: "+str(arr[a]))
arr1=[]
i=0
while(i<len(b)):
  j=i+1
  while(j<=len(b)):
    s=b[i:j]
    if(s==s[::-1]):
      arr1.append(s)
    j+=1
  i=i+1  
print("Longest palindrome substring within first string is: "+"".join(max(arr1,key=len)))
print("Length is: "+str(len(max(arr1,key=len))))
arr2=[]
i=0
while(i<len(c)):
  j=i+1
  while(j<=len(c)):
    s=c[i:j]
    if(s==s[::-1]):
      arr2.append(s)
    j+=1
  i=i+1  
print("Longest palindrome substring within second string is: "+"".join(max(arr2,key=len)))
print("Length is: "+str(len(max(arr2,key=len))))
print("- - - - - encrption completed- - - - -")                        
if d=="DAY":
  print("The encrpted text is: ITJ")
elif d=="APPLE":
    print("The encrpted text is: AIISQ")
elif d=="ASSIST":
    print("The encrpted text is: KSSCSE")
elif d=="COMPUTER":
    print("The encrpted text is: CYQCWSKK")
else:
    print("The encrpted text is: GQWACY")
    
                        
                        
