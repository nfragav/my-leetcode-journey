class Solution(object):
    def mergeKLists(self, lists):
        infinity = float('inf')
        values = [head.val if head else infinity for head in lists]
        head, current, current_min_node = None, None, None

        if not values:
            return head
        min_value = min(values)
        if min_value == infinity:
            return head

        min_i = values.index(min_value)
        current_min_node = lists[min_i]

        while current_min_node:
            if not current:
                head = ListNode(current_min_node.val)
                current = head
            else:
                current.next = ListNode(current_min_node.val)
                current = current.next
            
            lists[min_i] = lists[min_i].next
            if lists[min_i]:
                values[min_i] = lists[min_i].val
            else:
                values[min_i] = infinity
            
            min_value = min(values)
            min_i = values.index(min_value)
            current_min_node = lists[min_i]

        return head
