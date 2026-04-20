class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        raw = list()

        for l in lists:
            while l:
                raw.append(l.val)
                l = l.next

        raw.sort()

        dummy = ListNode()

        node = dummy
        for val in raw:
            node.next = ListNode(val)
            node = node.next

        return dummy.next
