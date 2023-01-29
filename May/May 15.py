class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        bthNode = None
        curr = list1
        while curr:
            curr = curr.next
            b-=1
            if b == 0: break
        bthNode = curr.next

        curr = list1
        while curr:
            if curr.next == None: 
                curr.next = bthNode
                break
            if a == 1:
                curr.next = list2
            curr = curr.next
            a-=1
        return list1
