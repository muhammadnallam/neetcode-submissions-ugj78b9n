class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []
        self.min = None
        

    def push(self, val: int) -> None:
        if self.min == None or val < self.min:
            self.min = val
        self.min_values.append(self.min)

        self.stack.append(val)
        return None
        

    def pop(self) -> None:
        print(self.min_values)
        self.min_values.pop()
        self.min = self.min_values[-1] if self.min_values else None
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
