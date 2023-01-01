def insertionSort(nums):
    nums = list(nums)
    
    for i in range(len(nums)):
        # Store the current element in a temporary variable
        cur = nums[i]
        
        # Find the correct position for the current element in the sorted sublist
        j = i-1
        while j >= 0 and nums[j] > cur:
            nums[j+1] = nums[j]
            j -= 1
        
        # Insert the current element into the correct position
        nums[j+1] = cur
    
    # Return the sorted list
    return nums