class Solution:
  def strStr(self,haystack, needle):
    h = len(haystack)
    n = len(needle)
    for i in range(h-n+1):
      segment = haystack[i:i+n]
      print(segment)
      if segment == needle:
        return i
    return -1
    
#O(n) time
#O(n) space
