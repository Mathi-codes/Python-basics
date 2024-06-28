a,b=map(int, input("Enter two numbers : ").split())
maxi=max(a,b)
lcm=maxi
while True:
    if maxi%a==0 and maxi%b==0:
        lcm=maxi
        break
print(lcm)
