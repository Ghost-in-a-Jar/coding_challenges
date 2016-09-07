"""This beat 100% of python submissions."""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        v1, v2 = l1.val, l2.val
        s = ListNode((v1 + v2) % 10)
        if v1 + v2 > 9:
            carry = 1
        else:
            carry = 0
        l1, l2 = l1.next, l2.next

        s_root = s

        while l1 != None or l2 != None:
            if l1 == None:
                v1 = 0
            else:
                v1 = l1.val
            if l2 == None:
                v2 = 0
            else:
                v2 = l2.val

            s.next = ListNode((carry + (v1 + v2) % 10) % 10)
            s = s.next
            try:
                l1 = l1.next
            except AttributeError:
                pass
            try:
                l2 = l2.next
            except AttributeError:
                pass
            if carry + v1 + v2 > 9:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            s.next = ListNode(1)
        return s_root
