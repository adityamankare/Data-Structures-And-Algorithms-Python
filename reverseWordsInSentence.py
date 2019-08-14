def reverseWordsInSentence(inputString):
  reverse = inputString[::-1]
  output = ' '.join(reverse)
  return print(output)

inputString = input().split(' ')
reverseWordsInSentence(inputString)
