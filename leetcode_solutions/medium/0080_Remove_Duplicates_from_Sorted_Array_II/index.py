def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i =0
    j=1
    counter=0
    while j < len(nums):
        #print(f'i-->{i},j-->{j},Counter-->{counter}')
        if nums[i] == nums[j]:
            if counter == 0:
                counter+=1
                i+=1
                nums[i] = nums[j]
        else:
            #print(f'nums[i]-->{nums[i]},nums[j]-->{nums[j]}')
            counter = 0
            i+=1
            nums[i] = nums[j]
        j+=1
        #print(nums)
    return i +1

def removeDuplicates_wrapper(nums):
    k = removeDuplicates(nums)
    return nums[:k]
