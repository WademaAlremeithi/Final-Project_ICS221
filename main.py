class Post:
    def __init__(self, datetime, post, post_owner, views):
        self.datetime = datetime
        self.post = post
        self.post_owner = post_owner
        self.views = views
        
#Binary Trees to use for binary search trees functions
#This would be used to find posts given a range of datetime
class Node:
    def __init__(self, data):
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.data = data
        
    def __repr__(self):
        return f"Node{self.data}"
        
    def find_min(self):
        current = self
        while current.l_child is not None:
           current = current.l_child
        return current

    def next_largest(self):
        if self.r_child is not None:
            return self.r_child.find_min()
        current = self
        while current.parent is not None and current is current.parent.r_child:
            current = current.parent
        return current.parent

#Binary Search Tree Class
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def to_string(self):
        if self.root is None:
            return 'Nil"
        self.print_tree(self.root, 0)

    def print_tree(self, root, depth):
        if not root: 
            return
        self.print_tree(root.r_child, depth + 1) 
        print('\t'* depth + '➡️ Node'+ str(root.data) +'')
        self.print_tree(root.l_child, depth + 1) 

    def insert(self, node):
        if type(node) is int:
            node = Node(node)

        if self.root is None:
            self.root = node
            return
        else:
            self.insert_node(node, self.root)
            
    def insert_node(self, node, root):
        if root.data >= node.data:
            if root.l_child is None:
            root.l_child = node
            node.parent = root
            else:
                self.insert_node(node,root.l_child))
        else:
            if root.r_child is None:
                root.r_child = node
                node.parent = root
            else:
                self.insert_node(node, root.r_child)
    def delete(self, value):
        node = self.search(value)
        if node is None:
            return None
        if node is self.root:
            pseudoroot = Node(None)
            pseudoroot.l_child = self.root
            self.root.parent = pseudoroot
            deleted = self.delete_node(self.root)
            self.root = pseudoroot.l_child
            if self.root is not None:
                self.root.parent = None
                return deleted
        else:
            return self.delet_node(node)

    def delete_node(self, node):
        if node.l_child is None or node.r_child is None:
            if node.parent.l_child is node:
                node.parent.l_child = node.l_child or node.r_child
                if node.parent.l_child is not None:
                    node.parent.l_child.parent = node.parent
            else:
                node.parent.r_child = node.r_child or node.l_child
                if node.parent.r_child is not None:
                    node.parent.r_child.parent = node.parent
            return node
        else:
            replacement = node.next_largest()
            replacement.data, node.data = node.data, replacement.data
            return self._delete_node(replacement)
    def search(self, value):
        if self.root is None:
            return None
        else:
            return self.search_value(value, self.root)

    def search_value(self, value, root):
        if not root:
            return None
        if value == root.data:
            return root
        elif value < root.data:
            return self.search_value(value, root.l_child)
        else:
            return self.search_value(value, root.r_child)

    def inorder(self):
        if not self.root:
            return []
        list = []
        root = self.root
        def sub_inorder(root):
            if root is not None:
                sub_inorder(root.l_child)
                list.append(root.data)
                sub_inorder(root.r_child)
        sub_inorder(root)
        return list
                
                            
        
