num=int(input("Enter a number : "))
dup=num
arm=0
length=len(str(num))
while num>0:
    last=num%10
    arm+=last**length
    num//=10
if dup==arm:
    print("armstrong number.. ")
else:
    print("Not a armstrong number..")