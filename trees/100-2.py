class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            return q is None
        if q is None:
            return p is None

        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
