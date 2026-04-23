class Solution:
    def isSame(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False
        return (
            a.val == b.val
            and self.isSame(a.left, b.left)
            and self.isSame(a.right, b.right)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
