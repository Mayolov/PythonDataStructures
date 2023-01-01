#the total number of comparisons is n^2-2n+1 which has the time complexity of o(n^2) additional space required is o(1)
def bubbleSort(nums):
    #creates copy of list
    nums = list(nums)
    
    for i in range(len(nums) -1):
        for j in range(len(nums)-1):
            if nums[i]> nums[i+1]:
                nums[i] = nums[i+1]
                nums[i+1] = nums[i]
    return nums