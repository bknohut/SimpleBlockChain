from djb2Hash import djb2

class MerkleNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class MerkleTree:
    def __init__(self):
        self.root = None

    def CreateTree(self, values):
        leaves = []
        for i in values:
            leaf = MerkleNode(djb2(i))
            leaves.append(leaf)

        return self._CreateTree(leaves)

    def _CreateTree(self, nodes):

        if len(nodes) == 1:
            self.root = nodes[0]
            return self.root

        items = []
        for i in range(0, len(nodes), 2):
            if i + 1 < len(nodes):
                data = djb2(nodes[i].data + nodes[i + 1].data)
                parent = MerkleNode(data)
                parent.left = nodes[i]
                parent.right = nodes[i + 1]
                nodes[i].parent = parent
                nodes[i + 1].parent = parent
                items.append(parent)
            else:
                data = djb2(nodes[i].data)
                parent = MerkleNode(data)
                parent.left = nodes[i]
                nodes[i].parent = parent
                items.append(parent)

        return self._CreateTree(items)

    def DFDisplayTree(self, node, index):
        if node is None :
            return ""
        return str(index) + " = " + node.data + "\n" + self.DisplayTree(node.left, index+1) + self.DisplayTree(node.right, index+1)

    def BFDisplayTree(self):
        if self.root is None:
            print("None")
            return
        q = [self.root]
        while len(q) > 0:
            print(q[0].data)
            if q[0].left is not None:
                q.append(q[0].left)
            if q[0].right is not None:
                q.append(q[0].right)
            q.pop(0)
