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
        return visited #visited

    def pre_order_iterative(self):
        # we use the stack to iterate on the visited nodes
        if not self.root:
            raise Exception("Tree is empty")
        stack = [self.root]
        visited =[]
        while stack:
            visited_node = stack.pop()
            visited.append(visited_node.value)
            if visited_node.left:
                stack.append(visited_node.left)
            if visited_node.right:
                stack.append(visited_node.right)
        return visited #visited

    def pre_order_recursive(self):
        # we use the iterations on the visited nodes
        if not self.root:
            raise Exception("Tree is empty")
        visited =[]
        def _transverse(node):
            if node:
                visited.append(node.value)
                _transverse(node.left)
                _transverse(node.right)
            return

        _transverse(self.root)
        return visited

    def in_order_iterative(self):
        # we use the stack to iterate on the visited nodes
        if not self.root:
            raise Exception("Tree is empty")
        current_node = self.root
        stack = []
        visited =[]
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                visited_node = stack.pop()
                visited.append(visited_node.value)
                if not visited_node.right:
                    continue
                current_node = visited_node.right
        return visited #visited

    def in_order_recursive(self):
        # we use the iterations on the visited nodes
        if not self.root:
            raise Exception("Tree is empty")
        visited =[]
        def _transverse(node):
            if node:
                _transverse(node.left)
                visited.append(node.value)
                _transverse(node.right)
            return

        _transverse(self.root)
        return visited

    def post_order_iterative(self):
        # we use the stack to iterate on the visited nodes
        if not self.root:
            raise Exception("Tree is empty")
        current =previous = self.root
        stack = []
        visited =[]
        while  current:
            while current.left:
                stack.append(current)
                current = current.left
            while not current.right or current.right == previous:
                visited.append(current.value)
                #print("current value", current.value)
                previous = current
                #print("previous value", previous)
                if not stack:
                    return visited
                current = stack.pop()
            stack.append(current)
            current = current.right
        return visited #visited

    def post_order_recursive(self):
        # we use the iterations on the visited nodes
        if not self.root:
            raise Exception("Tree is empty")
        visited =[]
        def _transverse(node):
            if node:
                _transverse(node.left)
                _transverse(node.right)
                visited.append(node.value)
            return

        _transverse(self.root)
        return visited

tree = TransversalTree()
tree.insert(29).insert(15).insert(44).insert(9).insert(22).insert(40).insert(49)\
   .insert(5).insert(10).insert(19).insert(27).insert(35).insert(46).insert(58)\
   .insert(8).insert(12).insert(21).insert(31).insert(39).insert(45).insert(2)
print(tree)
print("Breadth first transversal",tree.breadth_first_transversal())
print("pre order iterative ", tree.pre_order_iterative())
print("pre order recursive" , tree.pre_order_recursive())
print("in  order iterative" , tree.in_order_iterative())
print("in order recursive" , tree.in_order_recursive())
print("post order iterative", tree.post_order_iterative())
print("post order recursive" , tree.post_order_recursive())
