class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = [root]

        depth = 0
        while q:
            tq = []
            while q:
                node = q.pop()
                if node.left:
                    tq.append(node.left)
                if node.right:
                    tq.append(node.right)
            q = tq
            depth += 1

        return depth
