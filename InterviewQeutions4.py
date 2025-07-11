#reverse a string without uisng functions
string1 = "Ankithasshetty"
rev_string=""
for i in string1:
    rev_string =  i + rev_string
print(rev_string)

#find if one string is rotaion of another
def is_rotaion(s1,s2):
    s3=s1+s1
    #print(s1)
    if s2 in s3:
        return print(f"{s2} is rotation of {s1}")
    return print(f"{s2} is not a rotation of {s1}")
is_rotaion("abc","bac")

#strip all whitespaces from string
str1=" Anki tha s "
str1_whitestriped = str1.replace(" ","")
print(str1_whitestriped)

#longest substring without repeating character
def long_substring_withooutreap(str1):
    charSet= set()
    l=0
    lswr=0
    for r in range(len(str1)):
        while str1[r] in charSet:
            charSet.remove(str1[l])
            l +=1
        charSet.add(str1[r])
        lswr =max(lswr,r-l+1)
    return print(lswr)
long_substring_withooutreap("abcdaed")

