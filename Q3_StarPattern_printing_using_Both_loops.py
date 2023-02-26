# using For loop

n=int(input("Enter Matrix Size"))
for i in range(n+1,0,-1):
    for j in range(0,n+1):
        if(i>j):
            print(" ",end="")
        else:
            print("* ",end="")
    print()

# using While Loop

n=int(input("Enter Matrix Size"))
i=n+1
while i>0:
    j=0
    while j<n+1:
        if(i>j):
            print(" ",end="")
        else:
            print("* ",end="")
        j=j+1
    i=i-1
    print()
