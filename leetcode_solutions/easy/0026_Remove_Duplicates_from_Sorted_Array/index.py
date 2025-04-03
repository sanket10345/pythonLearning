nums = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3]

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i =0
    j=1
    while j < len(nums):
        if nums[i] == nums[j]:
            j+=1
        else:
            i+=1
            nums[i] = nums[j]
    return i +1

def removeDuplicates_wrapper(nums):
    k = removeDuplicates(nums)
    return nums[:k]
        