class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = head

        for _ in range(n):
            root = root.next

        if not root:
            return head.next

        pnth = head
        while root.next:
            root = root.next
            pnth = pnth.next

        pnth.next = pnth.next.next

        return head
