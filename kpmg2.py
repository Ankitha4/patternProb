s= [1,2,[3,4,[5,6]]]
def flatten_list(l):
    result=[]
    for i in l:
        if isinstance(i,list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
print(flatten_list(s))