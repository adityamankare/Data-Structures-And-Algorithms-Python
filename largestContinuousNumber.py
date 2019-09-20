def largest_continuous_sum(arr):
  # Input: [1,2,-1,3,4,10,10,-10,-1]
  # Output: 29
  currentSum = arr[0]
  maxSum = arr[0]

  for num in arr[1:]:

    currentSum = max(currentSum + num, num)
    maxSum = max(currentSum, maxSum)

  return maxSum

print(largest_continuous_sum([1,2,-1,3,4,10,10,-10,-1]))
