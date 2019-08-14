def mergeSort(inputList):
  if (len(inputList) < 2):
    return inputList

  result = []
  midpoint = int(len(inputList)/2)

  left = mergeSort(inputList[:midpoint])
  right = mergeSort(inputList[midpoint:])

  while (len(left) > 0) and (len(right) > 0):
    if (left[0] > right[0]):
      result.append(right.pop(0))   
    else:
      result.append(left.pop(0))

  result.extend(left + right)
  return result

inputList = list(map(int, input().split(',')))

print(mergeSort(inputList))
