"""
Level Order Traversal - BFS

A Tree Algorithm where the nodes in a tree are visited in a level by level fashion.
i.e Nodes at each level are processed before moving on to the next.

Steps
    1. For every node, add to a queue.
    2. Process the node and pop from the front of the queue.
    3. Add its left and right child to the queue.

Time complexity  is O(N) since we visit every node at least once. N is the number of nodes in the tree.
Space complexity is O(N) since we make use of a queue data structure having a maximum of size N. 


Sample Binary Tree:

      8
     / \
    3   10
   / \    \
  1   6    14

Level-Order Traversal of this binary tree results in:
output = [[8], [3,10], [1,6,14]]
"""

# Code implementation
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    import collections
    output = []
    queue = collections.deque([root])
    
    if root == None:
        return []
    
    while queue:
        num_of_nodes = len(queue)
        curr_level = []
        
        for node in range(num_of_nodes):
            curr_node = queue.popleft()
            curr_level.append(curr_node.val)
            
            if curr_node.left:
                queue.append(curr_node.left)
                
            if curr_node.right:
                    queue.append(curr_node.right)
        
        output.append(curr_level)
        

        
    return output
                