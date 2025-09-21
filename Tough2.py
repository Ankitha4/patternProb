#find the longest substring prefix in the string:
def longest_substring_prefix(s):
    max_prefix = ""
    if not s:
        return max_prefix
    min_word = min(len(word) for word in s)

    for i in range(min_word):
        c = s[0][i]
        for words in s:
            if words[i] != c:
                return max_prefix
        max_prefix += c
    return max_prefix

print(longest_substring_prefix(["Apple","Apply","Aptitude","Ape"]))