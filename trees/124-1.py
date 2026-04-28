class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))

            self.res = max(self.res, l + r + node.val)

            return max(l, r) + node.val

        dfs(root)
        return self.res
