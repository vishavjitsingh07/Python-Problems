class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        
        # Get node before middle node
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rootVal = slow.next.val # Root val for BST
        right = slow.next.next # Head for rigth child of BST
        slow.next = None # Trim left side to prepare left child of BST
        
        return TreeNode(
		    val=rootVal, 
		    left=self.sortedListToBST(head), 
		    right=self.sortedListToBST(right)
		)
