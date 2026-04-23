class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cur = 0
        res = []

        q = [root]
        nq = []

        while q:
            node = q.pop(0)
            if node.left:
                nq.append(node.left)
            if node.right:
                nq.append(node.right)

            if len(res) < cur + 1:
                res.append([node.val])
            else:
                res[cur].append(node.val)

            if not q and nq:
                q.extend(nq)
                nq.clear()
                cur += 1

        return res
