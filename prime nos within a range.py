x=int(input("enter a first number"))
y=int(input("enter a second number"))
print("prime numbers are")
while(x<=y):
    c=0
    i=1
    while(i<=x):
        if(x%i==0):
            c=c+1
        i=i+1
    if c==2:
        print(x)
    x=x+1
        
        
        
            
        

