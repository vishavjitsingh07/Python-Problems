class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        first = last = null = head
        counter = 1
        while null.next:
            null = null.next
            if counter < k:
                counter+=1
                first = null
            else: last = last.next

        first.val, last.val = last.val, first.val
        return head
