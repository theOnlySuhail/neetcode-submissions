# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow = fast = head

        while True:
            slow = slow.next
            fast = fast.next

            if fast is not None:
                fast = fast.next

            if slow is None or fast is None:
                return False

            if fast == slow:
                return True