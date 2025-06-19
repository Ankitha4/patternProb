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

#remove the duplicate word
str2="apple is sweet sweet fruit sweet"
str2_dup=[]
str2_list = str2.split(" ")
for word in str2_list:
    if word not in str2_dup:
        str2_dup.append(word)
str2_dup=" ".join(str2_dup)
print(str2_dup)

#remove the repeacting char:
str3="aaabbbcccdddeeffffaaaaaeeeeddddeeef"
str4=""
n=len(str3)
for char in range(n-1):
    if str3[char]!= str3[char+1]:
        str4 += str3[char]
str4 +=str3[-1]
print(str4)





