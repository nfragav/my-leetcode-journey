# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        e1 = l1
        e2 = l2

        result = e1.val + e2.val
        excess = result // 10
        result %= 10

        first_node = ListNode(result)
    
        e1 = e1.next
        e2 = e2.next
        if e1 or e2 or excess > 0:
            current_node = ListNode(excess)
            first_node.next = current_node

        while e1 or e2:
            result = current_node.val
            if e1:
                result += e1.val
            if e2:
                result += e2.val

            excess = result // 10
            result %= 10

            current_node.val = result

            if e1:
                e1 = e1.next
            if e2:
                e2 = e2.next
            
            if e1 or e2 or excess > 0:
                next_node = ListNode(excess)
                current_node.next = next_node
                current_node = next_node
        
        return first_node