# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        itr1 = l1
        itr2 = l2

        rem = 0
        while itr1 or itr2 or rem != 0:


            if not itr1:
                val1 = 0
            else:
                val1 = itr1.val
            if not itr2:
                val2 = 0
            else:
                val2 = itr2.val

            sum = val1 + val2 + rem

            if int(sum / 10) > 0:
                rem = 1
            else:
                rem = 0

            if itr1 == l1:
                headRes = ListNode(sum % 10, None)
                resEle = headRes
            else:
                newEle = ListNode(sum % 10, None)
                resEle.next = newEle
                resEle = newEle

            if itr1:
                itr1 = itr1.next
            if itr2:
                itr2 = itr2.next


        return headRes
