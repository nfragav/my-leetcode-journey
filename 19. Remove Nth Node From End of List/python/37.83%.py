# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        current = head
        lst = []
        new_head = head

        while current:
            lst.append(current)
            current = current.next
        
        if n > 1 and n < len(lst):
            left = lst[-n - 1]
            right = lst[-n + 1]
            left.next = right

        else:
            if len(lst) > 1:
                if n == 1:
                    lst[-2].next = None
                else:
                    new_head = lst[1]
            else:
                new_head = None

        return new_head

