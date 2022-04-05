# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.num = []
        

    def push(self, x: int) -> None:
        self.num.append(x)
        

    def pop(self) -> int:
        return self.num.pop(0)
        

    def peek(self) -> int:
        return self.num[0]
        

    def empty(self) -> bool:
        if len(self.num) != 0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()