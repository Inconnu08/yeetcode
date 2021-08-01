# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    fast = slow = head
# find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
# reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
# compare the first and second half nodes
    while node:  # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 1 2 3 3 2 1
        # 1 4 5 4 1

        # even
        # 1 2 3 4 5 6
        # fast = 3, 5
        # if fast == None, then we know it's even

        # odd
        # 1 2 3 4 5
        # fast = 3, 5
        # if fast != None, then odd

        fast = head
        slow = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next

            after = slow.next
            slow.next = rev
            rev = slow
            slow = after

        if fast:
            # move one over and ignore center
            slow = slow.next

        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next

        return not rev


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next  # move first, below will change structure
            rev, rev.next, slow = slow, rev, slow.next  # right is temporary parameter

        if fast:
            slow = slow.next
        while slow and rev and slow.val == rev.val:
            slow = slow.next
            rev = rev.next
        return not slow


# https://leetcode.com/problems/palindrome-linked-list/discuss/324358/O(n)-time-and-O(1)-space-with-explanation-(Python-and-C)
# https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space
