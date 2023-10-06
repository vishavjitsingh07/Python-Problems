class Solution:    
    def pairWiseSwap(self, head):
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            
            if prev:
                prev.next = temp
            else:
                head = temp
            
            prev = curr
            curr = curr.next
        
        return head
