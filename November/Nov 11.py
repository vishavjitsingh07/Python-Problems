class MyStack:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        return self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def empty(self) -> bool:
        return self.arr == []
