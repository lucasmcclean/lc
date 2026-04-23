class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        def dfs(node: 'TreeNode') -> 'TreeNode':
            if not node:
                return None
            if node == p or node == q:
                return node

            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                return node
            elif l:
                return l
            elif r:
                return r

            return None

        return dfs(root)
