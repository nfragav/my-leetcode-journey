class Solution(object):
    def swapPairs(self, head):
        if not head:
            return None
        elif head.next:
            new_head = head.next
        else:
            return head
        
        current = head
        past = None
        while current:
            if current.next:
                if past:
                    past.next = current.next
                following = current.next.next
                current.next.next = current
                if following:
                    if following.next:
                        current.next = following.next
                    else:
                        current.next = following
                    past = current
                    current = following
                else:
                    current.next = None
                    current = None
            else:
                current = None

        return new_head
        
