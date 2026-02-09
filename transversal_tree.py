from binary_search import BinarySearchTree, Node 
from collections import deque

class TransversalTree(BinarySearchTree):
    
    def breadth_first_transversal(self):
        if not self.root:
            raise Exception("Tree is empty")
        queue = deque()
        queue.append(self.root)
        visited =[]
        while queue:
            visited_node = queue.popleft()
            visited.append(visited_node.value)
            if visited_node.left:
                queue.append(visited_node.left)
            if visited_node.right:
                queue.append(visited_node.right)
        return True #visited


tree = TransversalTree()
tree.insert(29).insert(15).insert(44).insert(9).insert(22).insert(40).insert(49)\
   .insert(5).insert(10).insert(19).insert(27).insert(35).insert(46).insert(58)\
   .insert(8).insert(12).insert(21).insert(31).insert(39).insert(45)
print(tree)
if tree.breadth_first_transversal():
    print("all nodes visited")
