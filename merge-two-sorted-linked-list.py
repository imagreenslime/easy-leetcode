# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
class ListNode:
    # self-explanatory 0(m + n)
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        temp = cur = ListNode(0)
        while list1 and list2:
            # add the smaller number to the list then continue
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        # then add the remaining list
        return temp.next