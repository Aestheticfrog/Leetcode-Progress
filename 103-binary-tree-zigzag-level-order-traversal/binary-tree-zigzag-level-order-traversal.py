# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        res = []
        q = [root]
        ltor = True
        while q:
            curr = []
            temp = []
            for i in q:
                curr.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if not ltor:
                curr.reverse()
            res.append(curr)
            q = temp
            ltor = not ltor
        return res
