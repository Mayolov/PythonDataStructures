# quicksort works quickly for less than a certain amount of calls but quickly can cause a recursive error
# O(n log n) space complexity is O(n^2)
def quickSort(nums,start = 0, end = None):
    
    # Base case: if the list has 0 or 1 elements, it is already sorted
    if len(nums) <=1:
        return nums
    
    if end is None:
        nums = list(nums)
        end = len(nums)-1
        
    if start < end:
        pivot = partition(nums,start,end)
        quickSort(nums, start, pivot-1)
        quickSort(nums, pivot + 1, end)
        
    return nums

def partition(nums, start = 0, end = None):
    if end is None:
        end = len(nums)
    
    left = start
    right = end -1
    
    while right > left:
        if nums[left] <= nums[end]:
            left +=1
        elif nums[right]> nums[end]:
            right -=1
        
        else:
            nums[left] = nums[right]
            nums[right] = nums[left]
    
    if nums[left] > nums[right]:
        
        nums[left] = nums[end]
        nums[end] = nums[left]
        return left
    
    else:
        return end
    
    
    
    
        