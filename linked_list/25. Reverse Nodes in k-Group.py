# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = dummy = ListNode(next=head)

        # reverse s..e
        def reverse(s: ListNode, e: ListNode):
            last = None
            tail = s
            while s != e:
                next = s.next
                s.next = last
                last = s
                s = next
            s.next = last
            return s, tail

        # [dummy, 1, 2, 3, 4, 5], 2
        #    ↑    ↑  ↑  ↑
        #  curr   s  e next
        while True:
            s = e = curr.next
            for _ in range(k - 1):
                if e:
                    e = e.next
                else:
                    break
            if not e:
                break
            next = e.next
            left, right = reverse(s, e)
            curr.next = left
            right.next = next
            curr = right
        return dummy.next
