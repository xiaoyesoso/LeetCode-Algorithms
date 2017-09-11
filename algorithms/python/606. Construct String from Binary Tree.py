# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ""
        else:
            if t.left == None and t.right == None:
                return str(t.val)
            l= '()';r = ''
            if t.left != None:
                l = '('+self.tree2str(t.left)+')'
            if t.right != None:
                r = '('+self.tree2str(t.right)+')'
            return str(t.val)+l+r
