class LinkedList:
    class Node:
        def __init__(self, data: int):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = self.Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curNode = self.head.next
        idxCounter = 0
        while curNode is not None:
            if idxCounter == index:
                return curNode.data
            curNode = curNode.next
            idxCounter += 1
        return -1
    
    def insertHead(self, val: int) -> None:
        newNode = self.Node(val)
        newNode.next = self.head.next
        self.head.next = newNode

    def insertTail(self, val: int) -> None:
        curNode = self.head
        while curNode.next is not None:
            curNode = curNode.next
        curNode.next = self.Node(val)

    def remove(self, index: int) -> bool:
        curNode = self.head
        for i in range(index):
            if curNode is None:
                return False
            curNode = curNode.next
        if curNode is not None and curNode.next is not None:
            curNode.next = curNode.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        out = []
        curNode = self.head.next
        while curNode is not None:
            out.append(curNode.data)
            curNode = curNode.next
        return out
        
