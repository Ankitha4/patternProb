s= "ANKITHA S Shetty"
s=s.replace(" ","")
print(s)

def get_permutations(s):
    result = []
    def permute(path,remaining):
        if path:
            result.append(path)
        for i in range(len(remaining)):
            permute(path+remaining[i],remaining[:i]+remaining[i+1:])
    permute('',s)
    return result

def get_combinations(s):
    result = []
    def combine(path,index):
        if path:
            result.append(path)
        for i in range(index,len(s)):
            combine(path+s[i],i+1)
    combine('',0)
    return result
print(get_permutations("ABC"))
print(get_combinations("ABC"))


