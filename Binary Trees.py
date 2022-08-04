
class Tree():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    

leaf = Tree(None,None)
branch = Tree(leaf, leaf)
tree_1 = Tree(branch, leaf)
tree_2 = Tree(leaf, branch)
tree_3 = Tree(branch, branch)

"""
tree = tree_2
if tree.left == None:
    print ("leaf")
else:
    print("branch")
"""
tree = tree_2
#Number of leafs in a tree
def num_leaves(tree):
    if tree.left == None:
        return 1
    else:
        return num_leaves(tree.left) + num_leaves(tree.right)

#Number of edges
def num_edges(tree):
    if tree.left == None:
        return 0
    else:
        return 2 + num_edges(tree.left) + num_edges(tree.right)

#Number of nodes

def num_nodes(tree):
    if tree.left == None: 
        return 0
    else:
        return num_edges(tree)+ 1





if __name__ == "__main__":
    print("The binary tree has", num_leaves(tree) , "leaves")
    print("The binary tree has", num_edges(tree), "edges")
    print ("The binary tree has", num_nodes(tree), "nodes")

        