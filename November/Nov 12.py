#User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

def deleteNode(root, key):
    if(root==None):
        return root
    if(key<root.data):
        root.left=deleteNode(root.left, key)
    elif(key>root.data):
        root.right=deleteNode(root.right,key)
    else:
        if(root.left==None):
            tmp=root.right
            root=None
            return tmp
        elif(root.right==None):
            tmp=root.left
            root=None
            return tmp
            
        tmp=findNext(root.right)
        root.data=tmp.data
        root.right=deleteNode(root.right,tmp.data)
        
    if(root==None):
        return root
    
    root.height=1+max(getHeight(root.left),getHeight(root.right))
    
    bal=getBalance(root)
    
    #LL
    if(bal>1 and getBalance(root.left)>=0):
        return rotateRight(root)
    
    #LR
    elif(bal>1 and getBalance(root.left) < 0):
        root.left=rotateLeft(root.left)
        return rotateRight(root)
    #RR
    elif(bal<-1 and getBalance(root.right) <= 0):
        return rotateLeft(root)
    #RL
    elif(bal<-1 and getBalance(root.right) > 0):
        root.right=rotateRight(root.right)
        return rotateLeft(root)
    
    return root
    
def getHeight(root):
    if(root==None):
        return 0
    return root.height
    
def getBalance(root):
    if(root==None):
        return 0
    return getHeight(root.left)-getHeight(root.right)
            
def findNext(root):
    while(root and root.left):
        root=root.left
    return root
        
def rotateRight(root):
    x,y,z=root,root.left,root.left.left
    x.left=y.right
    y.right=x
    
    #updating heights after rotation
    x.height=1+max(getHeight(x.left),getHeight(x.right))
    y.height=1+max(getHeight(y.left),getHeight(y.right))
    return y

def rotateLeft(root):
    x,y,z=root,root.right,root.right.right
    x.right=y.left
    y.left=x
    
    #updating heights after rotation
    x.height=1+max(getHeight(x.left),getHeight(x.right))
    y.height=1+max(getHeight(y.left),getHeight(y.right))
    return y




