class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            self.diameter = max(self.diameter, l + r)

            return 1 + max(l, r)

        dfs(root)
        return self.diameter
