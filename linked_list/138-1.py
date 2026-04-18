class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {
            None: None
        }

        current = head
        while current:
            seen[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copy = seen[current]
            copy.next = seen[current.next]
            copy.random = seen[current.random]
            current = current.next

        return seen[head]
