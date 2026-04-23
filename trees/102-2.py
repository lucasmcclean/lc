class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res =  []
        q = collections.deque()
        q.append(root)

        while q:
            l = len(q)
            level = []
            for _ in range(l):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
