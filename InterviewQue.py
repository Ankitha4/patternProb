
#count the vowels in name
name="ANKITHA SHETTY"
vowels="aeiouAEIOU"
consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQURSTVWXYZ"
count_vowels = sum(1 for ch in name if ch in vowels)
count_consonants = sum(1 for ch in name if ch in consonant)
print(f"vowels {count_vowels}")
print(f"consonants {count_consonants}")

#character counts in a string
char_count={}
char_vowel_count={}
for char in name:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
print(char_count)
#prints vowles keys
for key in char_count:
    if key in vowels:
        char_vowel_count[key]=char_count[key]
print(char_vowel_count)

#find the largest word in string
def find_longest_word(text):
    words = text.split(" ")
    longest_word=""
    length_longest_word=0
    for word in words:
        if len(word)> len(longest_word):
            longest_word=word
    length_longest_word = len(longest_word)
    return print(f"{length_longest_word},{longest_word}")

find_longest_word("I love prgrogramming in python")

def find_long_small_word(text):
    words = text.split(" ")
    long_word=max(words,key=len)
    len_long_word=len(long_word)
    small_word=min(words,key=len)
    len_small_word=len(small_word)
    #length_longest_word = len(longest_word)
    return print(f"longest:{len_long_word},{long_word},smallest:{len_small_word},{small_word}")

find_long_small_word("I love prgrogramming in python")




