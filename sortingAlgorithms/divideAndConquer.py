# tim complexity is  O(n log n) space complexity is O(n)
def merge_sort(nums):
    
    # Base case: if the list has 0 or 1 elements, it is already sorted
    if len(nums) <=1:
        return nums
    
    # Make a copy of the list to avoid modifying the original
    nums = list(nums)

    # Split the list into two halves
    mid = len(nums)//2    
    left = nums[:mid]
    right = nums[mid:]
    
    #solve the problem for each half recursively
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    #combine results
    sorted_nums = merge(left_sorted, right_sorted)
    
    return sorted_nums

def merge(nums1, nums2):
    
    merged = []
    i = 0
    j = 0

    # While there are elements in both lists:
    while i < len(nums1) and j < len(nums2):
        # Compare the elements at the current indices
        if nums1[i] <= nums2[j]:
        # If the element in nums1 is smaller, append it to the merged list and move to the next element in nums1
            merged.append(nums1[i])
            i += 1
        
        else:
        # If the element in nums2 is smaller, append it to the merged list and move to the next element in nums2
            merged.append(nums2[j])
            j += 1
            
    # Append the remaining elements from nums1 and nums2 (if any) to the merged list
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    
    return merged + nums1_tail + nums2_tail