library={}
while True:
    print()
    print("Menu")
    print("1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List book by genre\n6. Quit")
    c=input("Enter your choice(1-6): ")
    if c=="1":
        print()
        a=input("Enter the title,genre,and price of the book(seperated by|): ")
        print()
        title,genre,price=a.split("|")
        title,genre,price=title,genre,float(price)
        library[title]=(genre,price)
        print("Added",title,"to the library.")
        print()
        item=library.items()
        for k,v in item:
            print(k,"(%s, $%0.2f)" % (v[0],v[1]),end="\n")
    elif c=="2":
        r=input("Enter the title of the book to remove:")
        print()
        if not r in library:
            print("Error:",r,"not found in the library.")
        else:
            print("Removed",r,"from the library.")
            del library[r]
            item=library.items()
            print()
            for k,v in item:
                print(k,"(%s, $%0.2f)" % (v[0],v[1]),end="\n")
    elif c=="3":
        i=input("Enter the title of the book: ")
        print()
        if not i in library:
            print("Error:",i,"not found in the library.")
        else:
            print("Title: ",i)
            print("Genre: ",library[i][0])
            print("Price: ",library[i][1])
    elif c=="4":
            item=library.items()
            print()
            for k,v in item:
                print(k,"(%s, $%0.2f)" % (v[0],v[1]),end="\n")
    elif c=="5":
        library1={}
        lg=input("Enter the genre to search for: ")
        print()
        item=library.items()
        for k,v in item:
            if v[0]==lg:
                library1[k]=v
        item1=library1.items()
        if len(item1)==0:
            print("No books found in",lg,"genre.")
        for k,v in item1:
            print(k,"(%s, $%0.2f)" % (v[0],v[1]),end="\n")
    elif c=="6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
print("Goodbye!")
