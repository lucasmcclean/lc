class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.di = 0

        def dfs(n):
            if not n:
                return 0
            l = dfs(n.left)
            r = dfs(n.right)
            self.di = max(self.di, l + r)
            return max(l, r) + 1

        dfs(root)
        return self.di
