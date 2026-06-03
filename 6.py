class SimpleBST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert_node(self, value):
        self.root = self._insert_recursive(self.root, value)
        print("Вставлено:", value)

    def _insert_recursive(self, node, value):
        if node is None:
            return self.Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        return node

    def find_smallest(self, node):
        while node.left is not None:
            node = node.left
        return node

    def print_tree(self):
        self._print_recursive(self.root, 0)
        print()

    def _print_recursive(self, node, level):
        if node is None:
            return
        self._print_recursive(node.right, level + 1)
        print("   " * level + str(node.value))
        self._print_recursive(node.left, level + 1)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.value, end=" ")
            self._inorder_recursive(node.right)


def main():
    tree = SimpleBST()

    print("ВСТАВКА")
    tree.insert_node(50)
    tree.insert_node(30)
    tree.insert_node(70)
    tree.insert_node(20)
    tree.insert_node(40)
    tree.insert_node(60)
    tree.insert_node(80)

    print("ДЕРЕВО")
    tree.print_tree()


if __name__ == "__main__":
    main()
