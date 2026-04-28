class Solution:
    def buildTree(self, preorder, inorder):
        index = {val: i for i, val in enumerate(inorder)}

        self.preIdx = 0

        def build(l: int, r: int):
            if l > r:
                return None

            root = TreeNode(preorder[self.preIdx])
            self.preIdx += 1

            mid = index[root.val]

            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)

            return root

        return build(0, len(inorder) - 1)
