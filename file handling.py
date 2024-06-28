a,b=map(int, input("Enter two numbers : ").split())
try : 
    print(a/b)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero...",e)
try :
    a=int(input("Enter a number : "))
    print(a)
except ValueError:
    print("Please enter a number..")
finally :
    print("Thankyou")
try :
    fp=open("sample.txt","r")
except FileNotFoundError:
    print("File not found..")
try :
    print(2+'a')
except TypeError:
    print("Please enter only numbers...")
