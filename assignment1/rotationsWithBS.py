# 1) We are going to check the center of the list then compare it to both ends if its less than
# we look into getting the we'll look into the left side of the list, else we're look a the right

# NEEDS WORK
# https://leetcode.com/problems/search-in-rotated-sorted-array/

from jovian.pythondsa import binary_search


def count_rotations_binary(nums):
    low = 0
    high = len(nums)- 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_number = nums[mid]
        print("lo:", low,", hi:",high, ",mid:",mid)
        if mid > 0 and low<high:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= mid_number <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= mid_number <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1



print("the list has been rotated:",count_rotations_binary(nums = [19,25,29,30,2,3,4,5,6,7,9,11,14]), "times")
