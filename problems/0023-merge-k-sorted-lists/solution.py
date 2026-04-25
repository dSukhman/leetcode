# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
       
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                temp.append(self.mergeTwoLists(l1, l2))
            lists = temp
        
        return lists[0]

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        llist = ListNode()
        cur = llist

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next

            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next
            
        cur.next = list1 if list1 else list2

        return llist.next
