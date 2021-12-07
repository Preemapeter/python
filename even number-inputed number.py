start=int(input("enter the first number:"))
end=int(input("enter the second number:"))
for num in range(start,end+1):
    if num%2==0:
        print(num)
