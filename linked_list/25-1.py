class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        res = head

        afterK = head
        current = head
        previous = None

        while True:
            for _ in range(k):
                if afterK is None:
                    return res
                afterK = afterK.next

            nxt = None
            insertAt = afterK
            tail = current

            for _ in range(k):
                nxt = current.next
                current.next = insertAt
                insertAt = current
                current = nxt

            if previous is not None:
                previous.next = insertAt
            else:
                res = insertAt

            previous = tail

        return res
