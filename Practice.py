from typing import List

name = "AnkithaxxxxxxSShetty"
char_count={}
for c in name:
    if c in char_count:
        char_count[c] +=1
    else:
        char_count[c] =1
result=""
uni_value: list[int]=[]
third_highest_value= []
for i in char_count.values():
    if i not in uni_value:
        uni_value.append(i)
if len(uni_value)<3:
    print("no 3rd highest element")
else:
    #sorting:
    for i in range(len(uni_value)-1,0,-1):
        for j in range(i):
            if uni_value[j]<uni_value[j+1]:
                uni_value[j],uni_value[j+1] = uni_value[j+1],uni_value[j]
    third_highest_count_valus=uni_value[2]
    for key,values in char_count.items():
        if values==third_highest_count_valus:
            third_highest_value.append(key)
    for c in name:
        if c not in third_highest_value:
            result +=c
    print(third_highest_count_valus)
    print(third_highest_value)
    print(result)

print(result.split())
print(char_count)
print(uni_value)

