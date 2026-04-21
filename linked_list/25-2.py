class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prevGroup = dummy

        while True:
            kth = prevGroup
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            nextGroup = kth.next

            cur, prev = prevGroup.next, kth.next
            while cur != nextGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp

        return dummy.next
