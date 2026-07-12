class MinStack:

    def __init__(self):
        self.items = []
        self.minstack = [] # initializing minimum stack to keep a track of minimum element across the stack
        

    def push(self, val: int) -> None:
        self.items.append(val)
        minval = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(minval)        

    def pop(self) -> None:
        self.items.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
        
