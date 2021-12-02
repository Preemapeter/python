a=int(input("enter the mark of MFC:"))
b=int(input("enter the mark of ADS:"))
c=int(input("enter the mark of ADS:"))
d=int(input("enter the mark of P Lab:"))
e=int(input("enter the mark Of ADS Lab:"))
total=a+b+c+d+e
avg=(total/5)
if(avg>80):
    print("A GRADE")
elif(avg<70):
    print("B GRADE")
elif(avg<60):
    print("C GRADE")
else:
    print("FAILED")
