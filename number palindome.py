num=int(input("Enter a number : "))
dup=num
reverse=0
while num>0:
    last=num%10
    reverse=reverse*10 + last
    num//=10
if reverse==dup:
    print("Palindrome...")
else:
    print("Not palindrome...")