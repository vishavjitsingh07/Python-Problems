# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge(l1, l2):
    head = l1
    curr = head
    l1 = l1.next
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
        else:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

    while l1:
        curr.next = l1
        l1 = l1.next
        curr = curr.next
    while l2:
        curr.next = l2
        l2 = l2.next
        curr = curr.next
    curr = head
    while curr:
        curr = curr.next
    return head

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(-10**4-1)
        arr = []
        for i in lists:
            if not i: continue
            if head.val < i.val:  head = merge(head, i)
            else: head = merge(i, head)

        return head.next


