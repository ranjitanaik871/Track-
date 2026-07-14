# Check whether two strings are anagrams

str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

if sorted(str1) == sorted(str2):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")