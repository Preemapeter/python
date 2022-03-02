a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
def thrice(a,b,c):
    s=a+b+c
    if(a==b==c):
        return(3*s)
    else:
        return(s)
print("sum=",thrice(a,b,c))
