# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#      self.left = left
#        self.right = right
class Solution:
    def __init__(self):
        self.listOfPaths = [] #this list will save all paths and return

    def binaryTreePaths(self, root: TreeNode, path="") -> List[str]:
        if(root==None):
            return [] #nothing to return (it's a empty node) ...
        
        path += " " + str(root.val)#actual node value becomes a 'element route'
        
        if(root.left==None and root.right==None):
            self.listOfPaths.append(path[1:].replace(" ", "->"))#question output format
    
        else:
            self.binaryTreePaths(root.left, path) #scan by route in left node
            self.binaryTreePaths(root.right, path)#scan by route in right node
        return self.listOfPaths #return all paths

