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
swd="applep"
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

#first non repeating character

reap_char="aaabssssvbbbbhnj"
len_str=len(reap_char)
for i in range(len_str):
    found=False
    for j in range(len_str):
        if i!=j and reap_char[i] == reap_char[j]:
            found=True
            break
    if not found:
        print(reap_char[i])
        break

#count how many times each character appears:
name = "Ankitha S Shetty"
char_count={}
for char in name:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

#Flip the words in a sentence, not letters:
Flip_words = "Flip the words in a sentence"
Flip_words_list = Flip_words.split()
rev = Flip_words_list[::-1]
rev = " ".join(rev)
print(rev)
Fl_wrds = []
for words in Flip_words_list:
    words = words[::-1]
    Fl_wrds.append(words)
Fl_wrds = " ".join(Fl_wrds)
print(Fl_wrds)

# Are two string Anagrams:
def find_anagram(str1,str2):
    str1_len = len(str1)
    str2_len = len(str1)
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1_len==str2_len and str1==str2:
        result = print("yes")
    else:
        result=print("No")
    return  result
find_anagram("Mug","gum")






