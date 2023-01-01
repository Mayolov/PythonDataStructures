import random
from bubbleSort import bubbleSort
from InsertionSort import insertionSort
from divideAndConquer import merge_sort
from quickSort import quickSort
list1 = [4, 2, 6, 3, 4, 6, 2, 1]
sortedList1 =  [1, 2, 2, 3, 4, 4, 6, 6]
list2 = [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
list3  = [3, 5, 6, 8, 9, 10, 99]
list4 = list(range(10000))


"""
a = bubbleSort(list1)
print(a)

b = bubbleSort(list2)
print(b)

c = bubbleSort(list3)
print(c)

d = bubbleSort(list4)
print(d)"""

"""
a = insertionSort(list1)
print(a)

b = insertionSort(list2)
print(b)

c = insertionSort(list3)
print(c)

d = insertionSort(list4)
print(d)"""
"""
a = merge_sort(list1)
print(a)

b = merge_sort(list2)
print(b)

c = merge_sort(list3)
print(c)

d = merge_sort(list4)
print(d)
"""

a = quickSort(list1)
print(a)

b = quickSort(list2)
print(b)

c = quickSort(list3)
print(c)

d = quickSort(list4)
print(d)