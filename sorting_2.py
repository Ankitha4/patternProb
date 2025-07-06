
#buble sort:
num=[23,4,5,67,90]
def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
    return print(num)
sort(num)


#selection sort:
nums = [5,6,8,9,7,4]
def sort(num):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
        tem=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=tem

        print(nums)
sort(nums)
print(nums)



