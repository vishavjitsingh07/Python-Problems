#User function Template for python3
'''
    Your task is to return the data stored in
    the nth node from end of linked list.
    
    Function Arguments: head (reference to head of the list), n (pos of node from end)
    Return Type: Integer or -1 if no such node exits.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    #code here

    fast=head
    while n-1 and fast:
        fast=fast.next
        n-=1
    if fast==None:
        return -1
    slow=head
    while fast.next:
        slow=slow.next
        fast=fast.next
    return slow.data
