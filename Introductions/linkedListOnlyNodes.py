# Nodes
# 1. Value - anything strings, integers, objects
# 2. The Next Node


class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

# "3" -> "7" -> "10"

node1 = linkedListNode("3") # "3"
node2 = linkedListNode("7") # "7"
node3 = linkedListNode("10") # "10"

node1.nextNode = node2 # node1 -> node2 , "3" -> "7"
node2.nextNode = node3 # node2 -> node3 , "7" -> "10"

# node1 -> node2 -> node3

head = node1
print "*********************************"
print "Traversing the regular linkedList"
print "*********************************"
# Regular Traversal
currentNode = head
while currentNode is not None:
    print currentNode.value,
    currentNode = currentNode.nextNode
print ''
print "*********************************"


def deleteNode(head, valueToDelete):
    currentNode = head
    previousNode = None
    while currentNode is not None:
        if currentNode.value == valueToDelete:
            if previousNode is None:
                newHead = currentNode.nextNode
                currentNode.nextNode = None
                return newHead
            previousNode.nextNode = currentNode.nextNode
            return head
        previousNode = currentNode
        currentNode = currentNode.nextNode
    return head # Value to delete was not found.

print "deleting the node '7'"
newHead = deleteNode(head, "0")


print "*********************************"
print "traversing the new linkedList with the node 7 removed"
print "*********************************"

currentNode = newHead
while currentNode is not None:
    print currentNode.value,
    currentNode = currentNode.nextNode