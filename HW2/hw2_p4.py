layers = int(input("Enter the number of layers(2 to 5)="))
length_top = int(input("Enter the side length of the top layer(2 to 6)="))
growth = int(input("Enter the growth of each layer="))
trunk_width = int(input("Enter the trunk width(odd number,3 to 9)="))
trunk_height = int(input("Enter the trunk height(4 to 10)="))
a = 2 * (length_top + growth * (layers - 1)) - 1
print("#".center(a))
n = 1
i = 1
if length_top==2:
  n=2
  print("###".center(a))
  while n<layers+1:
    while i<length_top+growth*(n-1)-1:
      print(("#"+"@"*(2*i-1)+"#").center(a))
      i=i+1
    if i==length_top+growth*(n-1)-1:
      print(("#"*(2*i+1)).center(a))
    n=n+1
    i=1
else:
  while n<layers+1:
    while i<length_top+growth*(n-1)-1:
      print(("#"+"@"*(2 * i - 1)+"#").center(a))
      i=i+1
    if i==length_top+growth*(n-1)-1:
      print(("#"*(2*i+1)).center(a))
    n=n+1
    i=1
w=0
while w<trunk_height+1:
  print(("|"*trunk_width).center(a))
  w = w + 1
