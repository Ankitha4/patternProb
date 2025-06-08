n = 5
#square
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()

#increasing Triangle:
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()

#decreasing Triangle:
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    print()

#increasing Triangle with space:
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()
    
#decreasing Triangle with space:
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n):
        print('*',end='')
    print()

#Hill patern
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()


#downward hill patern
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()


#Diamond Pattern
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()

