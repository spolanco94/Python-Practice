class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.helper_insert(self.root, new_val)

    def search(self, find_val):
        return self.helper_search(self.root, find_val)

    def print_tree(self):
        return self.preorder_print(self.root,"")[1:]
    
    def helper_search(self, start, find_val):
        print(type(self.right))
        if start.value == find_val:
            return True
        else:
            if start.value > find_val:
                if start.left:
                    return self.helper_search(start.left, find_val)
            else:
                if start.right:
                    return self.helper_search(start.right, find_val)

        return False
    
    def helper_insert(self, start, new_val):
        if self.search(new_val):
            print("Value already exists in tree.")
        else:
            if start.value > new_val:
                if not start.left:
                    start.left = new_val
                else:
                    self.helper_insert(start.left, new_val)
            else:
                if not start.right:
                    start.right = new_val
                else:
                    self.helper_insert(start.right, new_val)

    def preorder_print(self, start, traversal):
        if str(start.value) not in traversal:
            traversal = traversal + "-" + str(start.value)
        if start.left:
            traversal = self.preorder_print(start.left, traversal)
        if start.right:
            traversal = self.preorder_print(start.right, traversal)

        return traversal
    


# Set up tree
tree = BST(4)


# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)


# Check search
# Should be True
print(tree.search(4))

# Should be False
print(tree.search(6))

print(tree.print_tree())
