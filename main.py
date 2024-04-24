class Post:
    def __init__(self, datetime, post, post_owner, views):
        self.datetime = datetime
        self.post = post
        self.post_owner = post_owner
        self.views = views

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size 
        
    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))
            
    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]
        return None
        
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

class PostManager:
    def __init__(self):
        self.binary_search_tree = BinarySearchTree()
        self.hash_table = HashTable

    def add_post(self, post):
        self.binary_search_tree.insert(post.datetime)
        self.hash_table.insert(post.datetime, post)

    def find_post_by_datatime(self, datetime):
        return self.hash_table.search(datetime)

post_manager = PostManagger()
#test cases
sample_post = Post("24-4-2024  16:36", "Today is your opportunity to build the tomorrow you want. -Ken Poirot", "Sara Naser", 100)
post_manager.add_post(sample_post)
#find the post by its datetime
found_post = post_manager.find_post_by_datetime("24-4-2024  16:36")
if found_post:
    print("Found post: ", found_post.post)
else:
    print("Post not found.")
                                            
                            
        
