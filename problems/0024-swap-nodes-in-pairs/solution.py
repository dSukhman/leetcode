# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur and cur.next:
            second = cur.next

            # swap
            cur.next = second.next
            second.next = cur
            prev.next = second

            # move pointers
            prev = cur
            cur = cur.next

        return dummy.next
        