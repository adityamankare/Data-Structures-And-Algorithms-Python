def rotate(nums, k):
  nums.reverse()
  nums[:k] = reversed(nums[:k])
  nums[k:] = reversed(nums[k:])
  return nums

print(rotate([1,2,3,4,5,6,7],3))
#O(n) Time
#O(1) Space
