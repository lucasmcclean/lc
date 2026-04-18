class Solution:
    def addTwoNumbers(self, l1, l2):
        head = l1
        prev = None
        carry = 0

        while l1 or l2:
            if l1 and l2:
                l1.val += l2.val + carry
            elif l1:
                l1.val += carry
            else:
                prev.next = l2
                l1 = l2
                l2 = None
                l1.val += carry

            carry = l1.val // 10
            l1.val %= 10

            prev = l1
            l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            prev.next = ListNode(carry)

        return head
