class Solution:
    def insert(self,root,k):
        if(root.data==k):
            return
        elif(root.data>k):
            if(root.left):
                self.insert(root.left,k)
            else:
                root.left = Node(k)
                
        elif(root.data<k):
            if(root.right):
                self.insert(root.right,k)
            else:
                root.right = Node(k)
