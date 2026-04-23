class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = [root.val]
        q = collections.deque()
        q.append(root)

        while q:
            l = len(q)
            level = []
            for _ in range(l):
                node = q.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                res.append(level[-1].val)
                q.extend(level)

        return res
