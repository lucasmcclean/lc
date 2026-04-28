class Solution:
    def __init__(self):
        self.preord = None
        self.in_idxs = {}
        self.pre_idx = 0

    def build(self, l, r):
        if l > r:
            return None

        root = TreeNode(self.preord[self.pre_idx])
        self.pre_idx += 1

        piv = self.in_idxs[root.val]

        root.left = self.build(l, piv - 1)
        root.right = self.build(piv + 1, r)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.in_idxs[inorder[i]] = i
        self.preord = preorder
        return self.build(0, len(self.preord) - 1)
