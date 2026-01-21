class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(r):
            if not r:
                return

            r.left, r.right = r.right, r.left
            swap(r.left)
            swap(r.right)

        swap(root)
        return root
