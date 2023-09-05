class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        root = Node(0, head, None)
        
        size = 0
        while head:
            head.next = Node(head.val, head.next, head.random)
            head = head.next.next
            size += 1
            
        curr = root
        for _ in range(size):
            curr = curr.next.next
            if curr.random:
                curr.random = curr.random.next
            
        copy_root = Node(0, root.next.next, None)
        orig, copy = root.next, root.next.next
        for _ in range(size):
            orig.next = copy.next
            orig = orig.next
            copy.next = orig.next if orig else None
            copy = copy.next
            
        return copy_root.next
        
