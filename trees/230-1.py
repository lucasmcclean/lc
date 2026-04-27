class Solution:
    def __init__(self):
        self.res = None
        self.cur = 0

    def inorder(self, node, k):
        if not node or self.res:
            return
        self.inorder(node.left, k)
        self.cur += 1
        if self.cur == k:
            self.res = node
            return
        self.inorder(node.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root, k)
        return self.res.val
