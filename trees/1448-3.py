class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        nodes = [root]
        maxes = [root.val]
        res = 0

        while nodes:
            node = nodes.pop()
            seen = maxes.pop()

            if node.val >= seen:
                res += 1

            if node.left:
                nodes.append(node.left)
                maxes.append(max(node.val, seen))
            if node.right:
                nodes.append(node.right)
                maxes.append(max(node.val, seen))

        return res
