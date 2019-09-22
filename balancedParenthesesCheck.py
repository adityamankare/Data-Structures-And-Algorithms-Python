def balancedParenthesesCheck(s):
  #edge case check
  if len(s)%2 != 0:
    return False
  #initialize variables
  openingBrackets = set('({[')
  matchingPairs = set([('(',')'),('{','}'),('[',']')])
  #initialize stack (a list can be used as a stack here)
  stack = []
  #main code
  for parentheses in s:
    if parentheses in openingBrackets:
      stack.append(parentheses)
    else:
      if len(stack) == 0:
        return False
      lastOpenParentheses = stack.pop()
      #check if the pair exists in matchingPairs  
      if (lastOpenParentheses,parentheses) not in matchingPairs:
        return False
  #else return True
  return len(stack) == 0

print(balancedParenthesesCheck('{{{{(){[]}}}}}'))


