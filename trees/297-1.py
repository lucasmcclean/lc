class Codec:

    def serialize(self, root):
        def dfs(node, encoding):
            if not node:
                encoding.append("#")
                return

            encoding.append(str(node.val))
            dfs(node.left, encoding)
            dfs(node.right, encoding)

        encoding = []
        dfs(root, encoding)
        return "/".join(encoding)

    def deserialize(self, data):
        vals = iter(data.split("/"))

        def dfs():
            val = next(vals)
            if val == "#":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
