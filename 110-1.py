class Solution:
    def depth(self, node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(self.depth(node.left), self.depth(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        hl = self.depth(root.left)
        hr = self.depth(root.right)
        if abs(hl - hr) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
