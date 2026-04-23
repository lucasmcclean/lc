class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        dq = deque([root])

        while dq:
            level = []
            length = len(dq)

            for _ in range(length):
                node = dq.popleft()
                level.append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            res.append(level)

        return res
