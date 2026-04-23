class Solution:
    def isSame(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return self.isSame(t1.left, t2.left) and self.isSame(t1.right, t2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        same = self.isSame(root, subRoot)
        if same:
            return True

        if not root or not subRoot:
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
