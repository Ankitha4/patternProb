#linear sort

pos=-1
list1=[1,2,3,8,9]
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            #globals() ['pos'] = i
            return True
        i=i+1
    return False
n=3
if search(list1,n):
    print("Found at ",pos+1)
else:
    print("Not Found")


#binary sort:
pos=-1
list2=[2,45,78,90,105,90,20]
list2=sorted(list2)
def buble_search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                l=mid-1
    return False

if buble_search(list2,105):
    print("Found position",pos)
else:
    print("Not Found")





