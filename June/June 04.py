class Solution:
    def correctBST(self, root):
        # code here
        listt=[]
        def inorder(node):
            nonlocal listt
            if node.left:
                inorder(node.left)
            listt.append(node.data)
            if node.right:
                inorder(node.right)
        inorder(root)
        listt.sort()
        i=0
        def correction(node):
            nonlocal listt,i
            if node.left:
                correction(node.left)
                i+=1
            node.data=listt[i]
            if node.right:
                i+=1
                correction(node.right)
        correction(root)
        return root 
