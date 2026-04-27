class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            dfs(node.left)

            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return

            dfs(node.right)

        dfs(root)
        return self.res
