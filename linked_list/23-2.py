class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        res = ListNode()
        cur = res

        while heap:
            _, i, node = heapq.heappop(heap)

            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return res.next
