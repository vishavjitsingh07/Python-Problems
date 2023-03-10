class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.arr = []
        while self.head:
            self.arr.append(self.head.val)
            self.head = self.head.next
    def getRandom(self) -> int:
        return random.choice(self.arr)
