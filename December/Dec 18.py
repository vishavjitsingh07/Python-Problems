class Solution:
    
    def rearrange(self, head):
            
        altHead1 = Node(None)
        altHead2 = Node(None)
        
        current1 = altHead1
        current2 = altHead2
        
        while head: 
            current1.next = head
            current1 = current1.next
            
            if head.next:
                current2.next = head.next
                current2 = current2.next
            
            if head.next:
                head = head.next.next
            else:
                break
            
        temp = altHead2.next
        reverse = None
        while temp:
            next_node = temp.next
            temp.next = reverse
            reverse = temp
            temp = next_node
