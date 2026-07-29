# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(rt):
            if not rt:
                return 0
            l = dfs(rt.left)
            r = dfs(rt.right)
            nonlocal res
            res = max(res , l + r)
            return 1 + max(l , r)
        dfs(root)
        return res
