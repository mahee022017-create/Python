# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        s,b=[], []
        def pushleft(root):
            while root:
                s.append(root)
                root=root.left
        def pushright(root):
            while root:
                b.append(root)
                root=root.right
        pushleft(root)
        pushright(root)
        def getsmall():
            temp=s.pop()
            if temp.right:
                pushleft(temp.right)
            return temp.val
        def getbig():
            temp=b.pop()
            if temp.left:
                pushright(temp.left)
            return temp.val
        i=getsmall()
        j=getbig()
        while i<j:
            if i+j==k:
                return True
            elif i+j>k:
                j=getbig()
            else:
                i=getsmall()
        return False