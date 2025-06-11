#creating String
my_string='learning '
print(my_string)

#Concatenation:
str2='String'
print(my_string+str2)

#repeat the String
str3="Rep"
print(str3*3)

#length of the string:
str4="Ankitha"
count=0
#without len function
for i in str4:
    count=count+1
print(count)
print(len(str4))#using len keyword

#Accessing Index:
word="AccessingIndex"
print(word[3])#shoud print 4th char
print(word[-1])#shound pring last char

#slicing:
print(word[0:4])#print till 0 t0 3 [0,n]->0 to n-1
print(word[4:])#print till last
print(word[-3:])#prints last 3 char
print(word[::-1])#reverse String



