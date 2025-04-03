def reverse(nums,start,end):
    while start < end:
        tempHOld = nums[start]
        nums[start] = nums[end]
        nums[end] = tempHOld
        start+=1
        end-=1 
def rotate(nums,k):
    n = len(nums)
    k %= n
    reverse(nums,0,n -1)
    reverse(nums,0,k -1)
    reverse(nums,k,n -1)
    return nums
