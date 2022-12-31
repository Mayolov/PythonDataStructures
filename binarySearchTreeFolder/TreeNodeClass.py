class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        self.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        self.display_keys(self.left,space, level+1)    
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node
    
    def tree_height(self,node):
        if node is None:
            return 0
        return 1 + max(self.tree_height(node.left),self.tree_height(node.right))
    
    def min_height(self, node):
        if node is None:
            return 0
        if node.left is None or node.right is None:
            return max(self.minDepth(node.left), self.minDepth(node.right)) + 1
        else:
            return min(self.minDepth(node.left), self.minDepth(node.right)) + 1
        
    def diameterOfBinaryTree(self,node):
        if node is None:
            return 0
        self.diameter = 0
        self.get_diameter(node)
        return self.diameter-1
    
    def get_diameter(self,node):
        if node is None:
            return 0
        
        left = self.get_diameter(node.left)
        right = self.get_diameter(node.right)
        
        if left + right +1 > self.diameter:
            self.diameter = left +right + 1
        
        return max(left,right)+1