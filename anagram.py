str1=input("Enter the string 1 : ").lower()
str2=input("Enter the string 2 : ").lower()
if sorted(str1)==sorted(str2):
    print("Anagrams..")
else:
    print("Not anagrams..")