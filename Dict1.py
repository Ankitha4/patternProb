#reverse a string without using the slicing operation or reverse () function
def reverse_str(str1):
    result = ""
    for char in str1:
        result = char + result
    return result


print(reverse_str(str1="python"))