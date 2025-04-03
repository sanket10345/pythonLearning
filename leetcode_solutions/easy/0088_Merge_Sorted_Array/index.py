def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    m-=1
    n-=1
    k=m+n-1
    while (m >= 0 and n >= 0):
      if nums2[n] > nums1[m] :
         nums1[m+n + 2 -1] = nums2[n]
         n-=1
      else:
         nums1[m+n+ 2-1] = nums1[m]
         nums1[m] = nums2[n]
         m-=1
         n-=1

def merge_wrapper(nums1, m, nums2, n):
    merge(nums1, m, nums2, n)
    return nums1