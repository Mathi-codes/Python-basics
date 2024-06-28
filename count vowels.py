string=input("Enter the string : ")
count=0
for i in string:
    if i.lower() in 'aeiou':
        count+=1
print(count)