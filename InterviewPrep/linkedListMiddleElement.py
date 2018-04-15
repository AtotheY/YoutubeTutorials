class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode



def getMiddleElement(head):
    fastRunner = head
    slowRunner = head
    tick = False
    while fastRunner:
        fastRunner = fastRunner.nextNode
        if tick:
            slowRunner = slowRunner.nextNode
        tick = not tick
    return slowRunner.value


node1 = linkedListNode("3") # "3"
node2 = linkedListNode("7") # "7"
node3 = linkedListNode("10") # "10"

node1.nextNode = node2 # node1 -> node2 , "3" -> "7"
node2.nextNode = node3 # node2 -> node3 , "7" -> "10"

# 3->7->10

print getMiddleElement(node1)

