# using for loop
n=int(input("Enter Matrix Size"))
k=1
for i in range(n,0,-1):
    for j in range(0,n):
        if i>j:
            print(k,"\t",end="")
            k=k+1
    print()

# using while loop

n=int(input("Enter Matrix Size"))
k=1
i=5
while(i>=1):
    j=1
    while(j<=n):
        if i>j:
            print(k,"\t",end="")
            k=k+1
        j=j+1
    i=i-1
    print()