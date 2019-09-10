//First Approach
def anagram(string1,string2):
  # Remove spaces and lowercase letters
  string1 = string1.replace(' ','').lower()
  string2 = string2.replace(' ','').lower()
    
  # Return boolean for sorted match.
  return sorted(string1) == sorted(string2)

print(anagram('dog','god'))

//Second Approach
def anagram2(string1,string2):  
  # Remove spaces and lowercase letters
  string1 = string1.replace(' ','').lower()
  string2 = string2.replace(' ','').lower()
  # Edge Case to check if same number of letters
  if len(string1) != len(string2):
    return False
  # Create counting dictionary (Note could use DefaultDict from Collections module)
  count = {}  
  # Fill dictionary for first string (add counts)
  for letter in string1:
    if letter in count:
      count[letter] += 1
    else:
      count[letter] = 1      
  # Fill dictionary for second string (subtract counts)
  for letter in string2:
    if letter in count:
      count[letter] -= 1
    else:
      count[letter] = 1
  # Check that all counts are 0
  for k in count:
    if count[k] != 0:
      return False
  # Otherwise they're anagrams	
  return True

print(anagram2('clint eastwood','old west action'))
