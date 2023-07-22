#User function Template for python3
'''
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        d={}
        curr=head
        prev=None
        while curr!=None:
            if curr.data in d:
                prev.next=curr.next
                curr=curr.next
            else:
                d[curr.data]=1
                prev=curr
                curr=curr.next
        return head
