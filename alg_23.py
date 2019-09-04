# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None:
            return
        n = len(lists)
        return self.merge(lists, 0, n-1)
        
    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left)//2 #这里注意是求整
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
        
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        if l2.val < l1.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
