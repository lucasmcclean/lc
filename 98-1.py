class Solution:
    def validate(self, node, mn, mx) -> bool:
        if not node:
            return True

        if node.val <= mn or node.val >= mx:
            return False

        return self.validate(node.left, mn, node.val) and self.validate(node.right, node.val, mx)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float("-inf"), float("inf"))
