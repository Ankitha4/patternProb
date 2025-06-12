
#string Manipulation
text=" Ankitha shEtty "
print(text.upper()) #AllCapital
print(text.lower()) #Alllower
print(text.strip())#removes whitespace from both the edges
print(text.lstrip())#removes whitespace from left side
print(text.rstrip())#removes whitespace from right side

#Replace String
print(text.replace("shEtty","Shetty"))
print(text.replace("e","a"))

#Splitting and joining
data ="apple,bannana,chikku"
fruit_list= data.split(",")#split function now it will be tored in list
print(fruit_list)
print(".".join(fruit_list))

#Searching and Counting
texts="Programminp in Python"
find_py=texts.find("Python") #returns the staring index
print(find_py)
count_p=texts.count("P") # returns the count of P
print(count_p)
index_m=texts.index("m") #returs the first index of m
print(index_m)
if texts.startswith("Pro"): #checks is it starts with Pro
    print("Yes")
else:
    print("No")
if texts.endswith(("thon")):
    print("Yes")

#string Formatting
name="Ankitha"
age="25"
print(f"My name is {name} and my age is {age}")
print("My name is {} and my age is {}".format(name,age))


#iteration throgh string:
for char in "python":
    print(char)






