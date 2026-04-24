class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], mn: int, mx: int) -> bool:
            if not node:
                return True

            if not (node.val > mn and node.val < mx):
                return False

            return isValid(node.left, mn, node.val) and isValid(node.right, node.val, mx)

        return isValid(root, float("-inf"), float("inf"))
