#MERGE SORT

def splitList(inputList):
  lengthOfList = len(inputList)
  midpoint = lengthOfList//2
  leftList = inputList[:midpoint]
  rightList = inputList[midpoint:]
  return leftList,rightList


def mergeSortedLists(leftList, rightlist):
  leftList, rightList = splitList(inputList)
  #special case: if one or both lists are empty
  if (len(leftList) == 0):
    return rightlist
  elif (len(rightlist) ==0):
    return leftList
  #general case
  leftIndex = rightIndex = 0
  mergedList = []
  targetLengthOfList = len(leftList) + len(rightlist)
  while (len(mergedList) < targetLengthOfList):
    if (leftList[leftIndex] <= rightList[rightIndex]):
      mergedList.append(leftList[leftIndex])
      leftIndex += 1
    else:
      mergedList.append(rightList[rightIndex])
      rightIndex += 1

    #extreme case: if we are at one end of the list
    if (rightIndex == len(rightList)):
      mergedList += leftList[leftIndex:]
      break
    elif(leftIndex == len(leftList)):
      mergedList += rightList[rightIndex:]
      break
  return mergedList


def mergeSortAlgorithm(inputList):
  if (len(inputList) <= 1):
    return inputList
  else:
    left,right = splitList(inputList) 
    return mergeSortedLists(mergeSortAlgorithm(left), mergeSortAlgorithm(right))
  



inputList = input().split(',')
#left, right = splitList(inputList)
#print(left)
#print(right)

#mergedListVariable = mergeSortedLists(splitList(inputList))
#print('This is the merged list: ', mergedListVariable)

mergeSortAlgorithm(inputList)
print(mergeSortAlgorithm(inputList))
#print('This is the result', result)

