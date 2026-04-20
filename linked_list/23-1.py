class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        cur = res

        while any(lists):
            minVal = float("inf")
            minList = 0

            for i in range(len(lists)):
                if not lists[i]:
                    continue

                if lists[i].val < minVal:
                    minVal = lists[i].val
                    minList = i

            cur.next = lists[minList]
            cur = cur.next
            lists[minList] = lists[minList].next

        cur.next = None
        return res.next
