class Solution:
    def dfs(self, root, mx):
        if not root:
            return 0

        good = 1 if root.val >= mx else 0
        mx = max(mx, root.val)
        return good + self.dfs(root.left, mx) + self.dfs(root.right, mx)

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
