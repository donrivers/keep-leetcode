# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(None)
        cur_node = res
        while l1 and l2:
            if l1.val > l2.val:
                cur_node.next, l2 = l2, l2.next
            else:
                cur_node.next, l1 = l1, l1.next
            cur_node = cur_node.next
        if l1:
            cur_node.next = l1
        else:
            cur_node.next = l2
        return res.next
        
        
