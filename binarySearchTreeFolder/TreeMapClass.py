#__blank__ special funcs
from BSTClass import find, insert, list_all, update
from binaryTreePractice import balanceBST, display_keys, tree_size


class TreeMap():
    # initialize root
    def __init__(self) -> None:
        self.root = None
    
    #special set item function
    # combo of insert and update
    def __setitem__(self, key, value):
        node = find(self.root, key)
        
        # if key doesnt exist inside BST insert it
        if not node:
            self.root = insert(self.root,key, value)
            self.roof = balanceBST(self.root)
        else:
            update(self.root, key, value)
    
    # given a key return value
    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        # x for x in ()<- creates a generator and is used within a forloop
        return(x for x in list_all(self.root))
    
    def __len__(self):
        return tree_size(self.root)
    
    def display(self):
        return display_keys(self.root)
        
treemap = TreeMap()

