m=int(input("Enter the shopping amount: "))
l=input("Enter the membership level(Regular or Gold): ")
if l=="Regular":
    if m>3000:
        print("Regular "+"$"+str(m*0.80))
    elif m<=3000 and m>2000:
        print("Regular "+"$"+str(m*0.85))
    elif m<=2000 and m>1000:
        print("Regular "+"$"+str(m*0.9))
    elif m<=1000:
        print("Regular "+"$"+str(m))
elif l=="Gold":
    if m>3000:
        print("Gold "+"$"+str(m*0.75))
    elif m<=3000 and m>2000:
        print("Gold "+"$"+str(m*0.80))
    elif m<=2000 and m>1000:
        print("Gold "+"$"+str(m*0.85))
    elif m<=1000:
        print("Gold "+"$"+str(m))
else:
    print("Invalid member level.Please enter \'Regular\' or \'Gold\'")
