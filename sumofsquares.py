def sumofsquare(num):
    for i in range(1,num+1):
        if i**2 + (i+1)**2 == num:
            return True
    return False
num=int(input("Enter the number : "))
print(sumofsquare(num))