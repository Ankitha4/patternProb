#how to find all the substrings in the string and find palindromes
def findPalindrome(str1):
    n=len(str1)
    substring_list=[]
    for i in range(0,n):
        for j in range(i+1,n+1):
            substring_list.append(str1[i:j])
    for ch in substring_list:
        if ch==ch[::-1]:
            palindrome = print(f"{ch} is a palidrome")
    return palindrome
findPalindrome("Ankitha")

#initaie the empty list

list2 = list()
list1 =[1,2,23]
print(list1)
print(list2)
list2.extend([2,7,2,4,5,2,7,3])
print(list2)

#how to remove the duplicate if it has 2
for i in list2:
    if i==2:
        list2.remove(i)
print(list2)
list3=[]
for i in list2:
    if i not in list3:
        list3.append(i)
print(list3)





