class Deque:
    
    def __init__(self):
        self.queue = []


    def isEmpty(self) -> bool:
        return len(self.queue) == 0
        

    def append(self, value: int) -> None:
        self.queue.append(value)
        

    def appendleft(self, value: int) -> None:
        self.queue.insert(0, value)
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue.pop()

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.queue[0]
        self.queue.remove(val)
        return val
