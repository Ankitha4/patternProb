
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




