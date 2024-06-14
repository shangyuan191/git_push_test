import random
n=int(input("Enter the number of rows(N): "))
m=int(input("Enter the number of colmuns(M): "))
x=int(input("Enter the minimum number of obstacles(0-42): "))
print("Generated Mazed Map:")
matrix=[]
for i in range(n):
      matrix.append([" "]*m)      
def map(i):
    print("---".join(["+"]*(m+1)))
    for i in range(n):
        print("|"," | ".join(matrix[i-1]),"|")
        print("---".join(["+"]*(m+1)))
def obstacles():
    obst=[]
    for j in range(m):
        path=[]
        path.append([0,j])
    for i in range(n):
        path.append([m,i])
    while len(obst)<x:
        obs=[random.randint(0,n-1),random.randint(0,m-1)]
        if obs not in obst and obs not in path:
            obst.append(obs)
            r,c=obs
            matrix[r][c]="x"
obstacles()
map(i)
