class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = l1

        prev = l1
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
            else:
                prev.next = ListNode(0)
                l1 = prev.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            l1.val = total % 10
            prev = l1
            l1 = l1.next

        return res
