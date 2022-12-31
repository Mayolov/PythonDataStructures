from BSTClass import BSTNode
from TreeNodeClass import TreeNode
from BSTClass import list_all
    
            
def isBalanced(node):
    if node is None:
        return True, 0
    
    # checks if balanced on node.left or .right
    balanced_l, height_l = isBalanced(node.left)
    balanced_r, height_r = isBalanced(node.right)
    
    # the entire tree is balaced if the left and the right is balanced and the heights are 
    # less than or equal to one, to account for odd amounts
    balanced =  balanced_l and balanced_r and abs(height_l - height_r)<=1
    height = 1 + max(height_l,height_r)
    
    # boolean if balanced and height
    return balanced,height

def makeBalancedBST(data, low = 0, high = None, parent = None):
    
    if high is None:
        hi = len(data)-1
    if low> high:
        return None
    
    # look at the middle el
    # and make it the rood node
    mid = (low+high) // 2
    key, value = data[mid]
    
    # create a bst with the mid el as the root
    root = BSTNode(key,value)
    root.parent = parent
    
    # make the left half of the list and make a balanced bst
    root.left =  makeBalancedBST(data, low, mid-1,root)
    # make the left half of the list and make a balanced bst
    root.right = makeBalancedBST(data,mid+1,high,root)
    
    return root
    
    
def balanceBST(node):
    return makeBalancedBST(list_all(node))
    
def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)    
    
def parse_tuple(data):
    
    #print(data)# just to check how this works, not necessary
    # checks if data is type tuple and length is 3
    if isinstance(data,tuple) and len(data) == 3:
        
        # sets 2 as the key
        node = TreeNode(data[1])
        # call parse tuple with itself as the first el 
        # and sets the new key for the left side
        node.left = parse_tuple(data[0])
        # does the same as the top function
        node.right = parse_tuple(data[2])
    elif data is None: #if no data there is no node
        node = None
    else:# terminating condition of the recursive function
        node = TreeNode(data)
    return node

def tree_to_tuple(node):
    if node is None:
        return None
    return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))
        
def traverse_in_order(node):
    if node is None:
        return []
    
    #traverse the left subtree, returns list and makes a list of the node  then traverses the right node
    # end case is the none node
    return (traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

def tree_size(node):
    if node is None:
        return 0
    return 1+tree_size(node.left) + tree_size(node.right)
    


# Use this to add to the binary tree faster
# this is read as ((left subtree), key, (right subtree))
tree_tuple = ((1,3,None),2,((None,3,4),5,(6,7,8)))


tree2 = parse_tuple(tree_tuple)

james = tree_to_tuple(tree2)


print(james)
tree2.tree_height