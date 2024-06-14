s=input("Enter a sequence of integers seperated by whitespace: " )
a=list(map(int,s.split()))
r=[]
i=1
while i<len(a):
    if a[i]>a[i-1]:#找到那個斷崖，用i-1是怕out of range
        if i==(len(a)-1):#含最後一個數的那個串列也是遞增所以要append進去
            r.append(a)
        i=i+1
    else:
        r.append(a[:i])#append斷涯前面的遞增串列
        a=a[i:]#將a串列變成新的串列，沒有已經append的部分串列
        i=1
m=max(r,key=len)#在r中找出最長的遞增串列
print("Length: ",len(m))
print("LICS: ",m)
