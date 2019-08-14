def reverseWords(inputString):
  reverse = inputString[::-1]
  output = ' '.join(reverse)
  return print(output)

inputString = input().split(' ')
reverseWords(inputString)
