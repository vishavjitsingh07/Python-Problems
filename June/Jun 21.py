class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def cycleDetection(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return False
        
        slow = cycleDetection(head)
        if slow == False: return 
        slow2 = head
        while slow.next:
            if slow == slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next
        return
            
