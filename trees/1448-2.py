class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def goodCount(node: Optional[TreeNode], seen: int) -> int:
            if not node:
                return 0

            l = goodCount(node.left, max(seen, node.val))
            r = goodCount(node.right, max(seen, node.val))

            res = l + r
            if node.val >= seen:
                res += 1
            return res

        return goodCount(root, root.val)
