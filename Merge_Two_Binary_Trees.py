# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def fun(t1,t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t1.val=t1.val+t2.val
    t1.left=fun(t1.left,t2.left)
    t1.right=fun(t1.right,t2.right)
    return t1
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        t1=fun(t1,t2)
        return t1
        
        
            
