#reverse a string without using the slicing operation or reverse () function
'''
def reverse_str(str1):
    result = ""
    for char in str1:
        result = char + result
    return result


print(reverse_str(str1="python"))


#Write a prg to del all consonants from a given string
def del_consonants(str2):
    result =""
    consonants= "bcdfghjklmnpqrstvwxyz"
    str2 = str2.lower()
    for ch in str2:
        if ch not in consonants:
            result += ch
    return result

print(del_consonants("Python and Data Science"))
'''

def del_con(str3):
    vol = "aeiouAEIOU"
    res ="".join([char for char in str3 if not char.isalpha() or char in vol])
    return res

print(del_con("Python and Data Science 3"))
