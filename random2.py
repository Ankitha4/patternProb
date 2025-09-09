#write the program to find the sum of all the  prime number between 1 to N
def sum_prime(num):
    res =0
    for i in range(2,num+1):
        if num%i ==0:
            print(i)
            res +=i
    return res


print(sum_prime(10))

