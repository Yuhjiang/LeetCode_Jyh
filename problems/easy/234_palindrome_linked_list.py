class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = head
        elems = []

        while temp:
            elems.append(temp.val)
            temp = temp.next

        return elems == elems[::-1]
