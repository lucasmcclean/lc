class Solution:

    def depth(self, node: TreeNode) -> int:
        if not node:
            return 0

        return 1 + max(
            self.depth(node.left),
            self.depth(node.right)
        )

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(
            self.depth(root.left) + self.depth(root.right),
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )
