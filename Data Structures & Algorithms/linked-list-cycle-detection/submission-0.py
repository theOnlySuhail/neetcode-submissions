# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        is_visited = {}
        while head is not None:
            if is_visited.get(head):
                return True

            is_visited[head] = True
            head = head.next

        return False