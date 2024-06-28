def prime(num):
    count=0
    for i in range(2,num):
        if (num%i)==0:
            return 0
            break
    else:
        return 1
num1,num2=map(int,input("Enter two numbers : ").split())
lst=[]
for i in range(num1,num2):
    if prime(i):
        lst.append(i)
print(lst)