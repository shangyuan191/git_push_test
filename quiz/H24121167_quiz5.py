s=int(input("Enter the size of the grid: "))
g=[]
for i in range(s):
    g.append(["-"]*s)
for row in g:
    print(" ".join(row))
while True:
    c=str(input("Enter cell coordinates to edit: "))
    if c=="done":
        break
    v=str(input("Enter the new value for the cell: "))
    a,b=map(int,c.split(","))
    g[a][b]=v
    for row in g:
        print(" ".join(row))
