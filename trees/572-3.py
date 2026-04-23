class Solution:

    from hashlib import sha256

    def merkle(self, node: Optional[TreeNode]) -> str:
        if not node:
            return "#"
        l = self.merkle(node.left)
        r = self.merkle(node.right)
        h = self.sha256()
        h.update((f"{l},{node.val},{r}").encode())
        node.merkle = h.hexdigest()
        return node.merkle

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.merkle(root)
        self.merkle(subRoot)

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            return node.merkle == subRoot.merkle or (
                dfs(node.left) or dfs(node.right)
            )

        return dfs(root)
