#using for loop

n=int(input("Enter Matrix Size"))
for i in range(n+1,0,-1):
    for j in range(n+1,0,-1):
        if(i>j):
            print(" *",end="")
        else:
            print(" ",end="")
    print()


# using While loop

n=int(input("Enter Matrix Size"))
i=n+1
while i>0:
    j=n+1
    while j>0:
        if(i>j):
            print(" *",end="")
        else:
            print(" ",end="")
        j=j-1
    i=i-1
    print()