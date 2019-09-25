class Node:
  def __init__(self, value):
    self.value = value
    self.nextnode  = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


def nth_to_last_node(n, head):

  leftPointer = head
  rightPointer = head

  for i in range(n-1):
    if not rightPointer.nextnode:
      raise LookupError('Error: n is larger than the linkedlist')
    rightPointer = rightPointer.nextnode

  while rightPointer.nextnode:
    leftPointer = leftPointer.nextnode
    rightPointer = rightPointer.nextnode

  return leftPointer.value

print(nth_to_last_node(2, a))


    
