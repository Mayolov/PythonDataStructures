# returns the binary index of the first instance and last instance of a number 
# using an array thats in increasing order and contains multiples of a elements

def binary_search(lo,hi,condition):
    while lo<= hi:
        mid =(lo+hi)//2
        result = condition(mid)
         
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        else:                  
            lo = mid + 1
    return -1

def first_position (nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def main():
    print("Starting")

main()