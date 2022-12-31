# write a function that will check if a binary tree is a binary search tree
# white a function to find the max key in the binary tree
# write a function to find the min in the binary tree

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node): # takes a node
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)# Is it a BST, min val for left, max val for left
    is_bst_r, min_r, max_r = is_bst(node.right)# Is it a BST, min val for left, max val for left

    is_bst_node = (is_bst_l and is_bst_r and #if the left and right are bst's
                  (max_l is None or node.key> max_l) and # the max key is none or the current node is greater than the max
                  (min_r is None or node.key<min_r)) # min key is none or node is greater than the min
    
    min_key = min(remove_none([min_l,node.key,min_r])) # min of any of them
    max_key = max(remove_none([max_l,node.key,max_r])) # max of any of them
    
    return is_bst_node, min_key, max_key #returns if the node and the tree is a bst, the min key and max key from entire tree
    
#tree_tuple= ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

#tree = TreeNode.parse_tuple(tree_tuple)

"""biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')


tree = insert(None,jadhesh.username, jadhesh)

insert(tree,biraj.username, biraj)
insert(tree, hemanth.username, hemanth)

#tree.left = BSTNode(biraj.username, biraj)
#tree.left.parent = tree
#tree.right = BSTNode(hemanth.username, hemanth)
#tree.right.parent = tree

print(tree.key, tree.value)

display_keys(tree)"""