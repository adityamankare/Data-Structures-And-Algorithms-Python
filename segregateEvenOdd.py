def segregateEvenOdd(arr):
  left = 0
  right = len(arr) - 1
  while left < right:
    while arr[left]%2==0 and left < right:
      left += 1
    while arr[right]%2!=0 and left < right:
      right -= 1
    if left < right:
      arr[left], arr[right] = arr[right], arr[left]
      left += 1
      right -= 1
  return arr

print(segregateEvenOdd([12, 34, 45, 9, 8, 90, 3]))

#O(n) time
#O(1) space
