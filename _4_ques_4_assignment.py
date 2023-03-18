"""Count number of trees in a forest"""

# class to represent a node in the forest 
class Node: 

    def __init__(self, key): 
        self.key = key 
        self.children = []

# function to count the number of trees in the forest 
def count_trees_in_forest(forest): 

    # check if forest is empty 
    if len(forest) == 0: 
        return 0

    # create a dictionary to store the nodes in the forest 
    nodes = {} 

    # create a node object for each node in the forest 
    for i in range(len(forest)): 
        nodes[i+1] = Node(i+1) 

    # build the tree structure for the forest 
    for i in range(len(forest)): 
        if forest[i] != 0: 
            nodes[forest[i]].children.append(nodes[i+1]) 

    # perform DFS on each node in the forest to count the number of trees 
    tree_count = 0 

    for i in range(len(forest)): 
        if nodes[i+1] is not None and len(nodes[i+1].children) == 0: 
            stack = [] 
            stack.append(nodes[i+1]) 

            while len(stack) > 0: 
                current_node = stack.pop() 

                for child in current_node.children: 
                    stack.append(child) 

                current_node.children = [] 

            tree_count += 1 

    return tree_count 

# asking user to input the forest as a list of integers 
forest = list(map(int, input("Enter the forest as a list of integers: ").split())) 

# call the function to count the number of trees in the forest 
count = count_trees_in_forest(forest) 

# print the result 
print("Number of trees in the forest:", count) 
