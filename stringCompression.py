#STRING COMPRESSION
def compress(s):
  """
  Solved using the Run Length Compression Algorithm
  """

  result = ""

  if len(s) == 0:
    return ""

  if len(s) == 1:
    return s + '1'

  count = 1

  i = 1
  while i < len(s):
    if s[i] == s[i-1]:
      count += 1
    else:
      result = result + s[i-1] + str(count)
      count = 1
    i += 1
  result = result + s[i-1] + str(count)
  
  return result


print(compress('AAABBCCCC'))
