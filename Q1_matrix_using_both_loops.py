# using while loop
n=int(input("Enter Matrix Size"))
k=1
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(k," ",end="")
        k=k+1
        j=j+1
    i=i+1
    print()

# using for loop

n=int(input("Enter Matrix Size"))
k=1
for i in range(0,n):
    for j in range(0,n):
        print(k," ",end="")
        k=k+1
    print()