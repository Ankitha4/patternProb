#remove only integer repeating values from string
s="auuttt23ty222333555666678tybnnm321bb"
seen_int=[]
result_list=[]
for i in s:
    if i.isdigit():
        if i not in seen_int:
            seen_int.append(i)
            result_list.append(i)
    else:
        result_list.append(i)
result_list = "".join(result_list)
print(result_list)

#or
s="auuttt23ty222333555666678tybnnm321bb"
seen_integer =set()
res_list=[]
for char in s:
    if char.isdigit():
        num =int(char)
        if num not in seen_integer:
            seen_integer.add(num)
            res_list.append (char)
    else:
        res_list.append(char)
result ="".join(res_list)
print(result)