# Counts min roations of a list using effecient linear search.
def count_rotations(listy):
    # min is O(N) because it bascally does a for loop, but its faster than a for loop
    # binary search for the smallest int would be a better approach in this instance
    return listy.index(min(listy))

print("the list has been rotated:",count_rotations(listy = [19,25,29,3,5,6,7,9,11,14]), "times")


