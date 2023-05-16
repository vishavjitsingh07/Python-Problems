class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        newHead = head.next
        temp = newHead.next
        newHead.next = head
        head.next = temp
        while head and head.next:
            try:
                curr = head.next
                swapNode = curr.next
                temp = swapNode.next
                head.next = swapNode
                swapNode.next = curr
                curr.next = temp
                head = curr
            except: break
        return newHead
