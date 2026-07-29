# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        def bst(front,back):
            if front > back:
                return None
            mid = front + (back - front) // 2
            root = TreeNode(l[mid])
            root.left = bst(front,mid - 1)
            root.right = bst(mid + 1,back)
            return root
        return bst(0,len(l) - 1)