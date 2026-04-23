class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        dq = deque([root])

        while dq:
            tq = deque()
            level = []

            while dq:
                node = dq.popleft()
                level.append(node.val)

                if node.left:
                    tq.append(node.left)
                if node.right:
                    tq.append(node.right)

            res.append(level)
            dq = tq

        return res
