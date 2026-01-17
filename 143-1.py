class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Find middle of list
        mid = head
        double = head
        while double != None and double.next != None:
            double = double.next.next
            mid = mid.next

        # Reverse second half of list
        prev = None
        while mid.next != None:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        mid.next = prev

        # Interleave the lists
        while mid.next != None:
            hnext = head.next
            mnext = mid.next
            head.next = mid
            mid.next = hnext
            head = hnext
            mid = mnext
