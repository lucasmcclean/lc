class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        dq = deque([root])

        while dq:
            res.append(dq[-1].val)

            length = len(dq)

            for _ in range(length):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return res
