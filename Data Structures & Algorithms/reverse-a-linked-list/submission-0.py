# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curNode = head
        prev = None
        while curNode:
            nxt = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = nxt
        return prev