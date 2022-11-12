# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        tab = []
        p = list1
        q = list2
        
        resHead = None
        
        while p:
            tab.append(p.val)
            p = p.next
        
        while q:
            tab.append(q.val)
            q = q.next
        
        tab.sort()
        check = 1
        
        for i in tab:
            
            if check == 1:
                resHead = ListNode(i,None)
                res = resHead
                check = 0
            else:
                res.next = ListNode(i,None)
                res = res.next
            
        
        return resHead
            
                
            
            