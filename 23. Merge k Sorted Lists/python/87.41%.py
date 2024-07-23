class Solution(object):
    def mergeKLists(self, lists):
        lst = []
        for node in lists:
            while node:
                lst.append(node.val)
                node = node.next
        
        if not lst:
            return None
            
        lst.sort()
        head = None
        for value in lst:
            if not head:
                head = ListNode(value)
                current = head
            else:
                current.next = ListNode(value)
                current = current.next

        return head
