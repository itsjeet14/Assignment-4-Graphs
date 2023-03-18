"""Count the number of nodes at given level in a tree using BFS"""

from collections import deque 

# class to represent a node in the tree 
class Node: 

    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None

# function to count the number of nodes at a given level in the tree 
def count_nodes_at_level(root, level): 

    # check if root is None 
    if root is None: 
        return 0

    # create a queue to store the nodes at each level 
    q = deque() 
    q.append(root) 

    # level of the root node is 1 
    node_level = 1 
    node_count = 0 

    # perform BFS to traverse the tree level by level 
    while len(q) > 0: 

        # get the number of nodes at the current level 
        current_level_size = len(q) 

        # traverse all the nodes at the current level 
        for i in range(current_level_size): 
            current_node = q.popleft() 

            # check if the current node is at the given level 
            if node_level == level: 
                node_count += 1 

            # add the children of the current node to the queue 
            if current_node.left is not None: 
                q.append(current_node.left) 
            if current_node.right is not None: 
                q.append(current_node.right) 

        # increment the level counter after all nodes at the current level have been traversed 
        node_level += 1 

    return node_count 

# asking user to input the level they want to count nodes at
level = int(input("Enter the level you want to count nodes at: "))

# create a sample binary tree for testing 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 

# call the function to count the number of nodes at the given level 
count = count_nodes_at_level(root, level) 

# print the result 
print("Number of nodes at level", level, ":", count) 
