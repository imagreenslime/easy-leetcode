# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, curr: Optional[ListNode]) -> Optional[ListNode]:
        answer = dummy = ListNode(0)
        answer.next = curr
        while curr and curr.next:
            if curr.next.val == curr.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                curr = curr.next
                # we dont set the dummy to the next int until we know that the next number isnt a duplicate
                # so the while loop will continue until so
                dummy.next = curr
            else:
                curr = curr.next
                dummy = dummy.next
        return answer.next