# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        current1 = list1
        current2 = list2
        current_new = None
        head = None

        while current1 or current2:
            if current_new:
                current_new.next = ListNode()
                current_new = current_new.next
            else:
                current_new = ListNode()
                head = current_new

            if current1 and current2:
                if current1.val <= current2.val:
                    current_new.val = current1.val
                    current1 = current1.next
                else:
                    current_new.val = current2.val
                    current2 = current2.next

            elif current1:
                current_new.val = current1.val
                current1 = current1.next

            elif current2:
                current_new.val = current2.val
                current2 = current2.next

            
        return head
