def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
num=input("Enter the number :" )
lst=[]
for i in num:
    lst.append(fact(int(i)))
print(sum(lst))