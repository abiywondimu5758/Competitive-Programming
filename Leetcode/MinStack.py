class MinStack:

    def __init__(self):
        self.minStack = []
        self.min = None
        

    def push(self, val: int) -> None:
        if len(self.minStack ) == 0:
            self.minStack.append(val)
            self.min = val
        else:
            if self.min <= val:
                self.minStack.append(val)
            else:
                self.minStack.append(2*self.min -self.minStack[-1])
                self.min = val
        

    def pop(self) -> None:
        if len(self.minStack) != 0:
            if self.minStack[-1] >= self.min:
                self.minStack.pop()
            else:
                self.min = 2*self.min -self.minStack[-1]
                self.minStack.pop()
        
        

    def top(self) -> int:
        if len(self.minStack) != 0:
            if self.minStack[-1] >= self.min:
                return self.minStack[-1]
            else:
                return self.min
        else:
            return None

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
