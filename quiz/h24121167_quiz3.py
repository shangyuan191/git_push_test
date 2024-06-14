print("Welcome to the simple calculator program!")
while True:#如果沒出現break此回圈就會一直執行
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    c=input("Select an arithmetic operation(+,-,*,/): ")
    if c=="+":
        d=a+b
        print("Result: "+str(float(d)))
        q=str(input("Do you want to perform another calculation?(yes or no): "))
        if q!=str("yes"):
            break
    elif c=="-":
        d=a-b
        print("Result: "+str(float(d)))#float 使計算結果出現小數點
        q=str(input("Do you want to perform another calculation?(yes or no): "))
        if q!=str("yes"):
            break
    elif c=="*":
        d=a*b
        print("Result: "+str(float(d)))
        q=str(input("Do you want to perform another calculation?(yes or no): "))
        if q!=str("yes"):
            break
    elif c=="/":#除法回圈需注意第二項是否為零所以加一個判斷程式除法回圈需注意第二項是否為零所以加一個判斷程式
        if b==0:
            print("Error:Division by zero!")
            q=str(input("Do you want to perform another calculation?(yes or no): "))
            if q!=str("yes"):
                break
        else:
            d=a/b
            print("result: "+str(float(d)))
            q=str(input("Do you want to perform another calculation?(yes or no): "))
            if q!=str("yes"):
                break
    else:
        q=str(input("Do you want to perform another calculation?(yes or no): "))
        if q!=str("yes"):
            break
print("Goodbye!")        
      
        
        
