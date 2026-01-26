class Solution:
    def dfs(self, node: Optional[TreeNode]) -> (bool, int):
            if not node:
                return (True, 0)

            lb, lh = self.dfs(node.left)
            rb, rh = self.dfs(node.right)
            return (lb and rb and abs(lh - rh) <= 1, 1 + max(lh, rh))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
