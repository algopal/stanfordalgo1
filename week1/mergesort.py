"""
Implementation of merge sort in python
"""

def mergesort(alist):
  """
  alist: list of numbers that needs to be sorted
  """
  l = len(alist)
  if l <= 1:
    return alist
  left_sorted = mergesort(alist[:l/2])
  right_sorted = mergesort(alist[l/2:])
  
  i = j = k = 0
  
  while k < len(alist):
    if i < len(left_sorted) and j < len(right_sorted):
      if left_sorted[i] < right_sorted[j]:
        alist[k] = left_sorted[i]
        i += 1
      else:
        alist[k] = right_sorted[j]
        j += 1
    elif i == len(left_sorted) - 1 and j < len(right_sorted):
      alist[k] = right_sorted[j]
      j += 1
    elif j == len(right_sorted) - 1 and i < len(left_sorted):
      alist[k] = left_sorted[i]
      i += 1

    k += 1
  
  return alist

print mergesort([1,5,2,5,7,32,2,34,2,45,11,6])
