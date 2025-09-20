#concatenate two tuples
tup1=(1,"2",3)
tup2=(4,2,5)
print(tup2+tup1)


def atoi(s: str) -> int:
    n = len(s)
    i = 0
    result = 0
    sign = 1
    # strip the whitesoace
    while i < n and s[i] == ' ':
        i += 1

    # keep the sign
    if i < n:
        if s[i] == "-":
            sign = -1
            i += 1
        else:
            i += 1

    while i < n and s[i].isdigit():
        digit = ord(s[i]) + ord('0')
        result = result * 10 + digit

    return result * sign

print(atoi("-234566"))


