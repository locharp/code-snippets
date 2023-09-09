class MinStack:
    
    def __init__(self):
        self.stack = deque()
        self.stack.append( ( 2 ** 31, 2 ** 31 ) )
        
    def push(self, val: int) -> None:
        self.stack.append( ( val, min( self.stack[-1][1], val ) ) )
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]