size = int(input("Enter the size of the pattern:"))
x = 0
while x < size:
    j=0
    while j < size:
        print("*",end="")
        j+=1
    print()
    x+=1
