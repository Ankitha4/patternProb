# reverse a string
str=("Ankitha Shetty")
str_rev=str[::-1]
print(str_rev)

#reverse a number of elements
list1=[1,2,3,4]
rev_list1=list1[::-1]
print(rev_list1)

#palindrome or not
str1 = "malayal"
rev_str1 = str1[::-1]
if str1 == rev_str1:
    print(f"{str1} is a palindrome")
else:
    print(f"{str1} is not a palindrome")

#remove the duplicate
swd="apple"
swtd=""
for i in swd:
    if i not in swtd:
        swtd += i
print(swtd)

