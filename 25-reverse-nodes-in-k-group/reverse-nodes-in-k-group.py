# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        while count >= k:
            curr = prev.next
            temp = curr.next
            for _ in range(1,k):
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
                temp = curr.next
            prev = curr
            count -= k
        return dummy.next
        
