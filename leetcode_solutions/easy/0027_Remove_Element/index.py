def remove_element(nums,val):
    k=0
    for num in nums:
        if(num != val):
          nums[k] = num
          k +=1
    return k
