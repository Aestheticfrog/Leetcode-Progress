# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        BST = True
        temp = root
        stack = []
        prev = float("-inf")
        while BST and (stack or temp):
            while temp:
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            if temp.val <= prev:
                BST = False
                break
            prev = temp.val
            temp = temp.right
        return BST


        