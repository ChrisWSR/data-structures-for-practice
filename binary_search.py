class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):

        self.root = None
    def __str__(self):
        if not self.root:
            return "Empty tree"
        return self._tree_string(self.root,"",True)
    def _tree_string(self,node,prefix,is_tail):
        """Helper method to build tree visualization """
        if not node: 
            return "" 
        result = prefix + ("└──" if is_tail else "├──") + str(node.value) + "\n"
        # Get children
        children = []
        if node.left:
            children.append(('left', node.left))
        if node.right:
            children.append(('right', node.right))

        for i, (side,child) in enumerate(children):
            is_last =(i == len(children) - 1)
            extension = "    " if is_tail else"│  "
            result += self._tree_string(child, prefix + extension,is_last)
        return result

    def insert(self,value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self
        current_node = self.root
        while value !=current_node.value:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    break
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    break
                current_node = current_node.right
        return self
    def contains(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return True
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
    def remove(self,value,start=None, parent=None):
        current = start or self.root
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = parent.left
            else:
                current = parent.right
        if not current:
            raise Exception("Item not in tree")
        if not current.right and not current.left:
            return self._remove_node_no_children(current,parent)
        if current.right and current.left:
            return self._remove_node_two_children(current)
        return self._remove_node_one_child(current,parent)
   # remove with no childs no conexions
    def _remove_node_no_children(self,current,parent):
        if current is self.root:
            self.root = None
            return self
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None
        return self
    # remove with o
    def _remove_node_one_child(self,current,parent):
        if current is self.root:
            self.root = current.right if current.right else current.left
            return self
        if parent.right == current:## check if the value its all the right of the parent 
            parent.right = current.right if current.right else current.left # if this conditions its complete then move the child to the right on the parent making the new child
        else:
            parent.left = current.right if current.right else current.left
        return self
    #check for the successor of the value to be deleted and then replace it and delete it from the tree
    def _remove_node_two_children(self,current):
        successor = self._get_successor(current)
        current.value = successor.value
        return self.remove(successor.value,start=current.right,parent=current) 


    @staticmethod
    def _get_successor(current):
        successor = current.right
        while successor and successor.left:        
            successor = successor.left
        return successor



##tree = BinarySearchTree()
#
##tree.insert(20).insert(19).insert(2).insert(4)
##tree.insert(10).insert(49).insert(1).insert(5)
##print(tree.contains(4))
##print(tree.contains(3))
##print(tree)                           
#bst = BinarySearchTree()
#bst.insert(29).insert(15).insert(44).insert(9).insert(22).insert(40).insert(49)\
#   .insert(5).insert(10).insert(19).insert(27).insert(35).insert(46).insert(58)\
#   .insert(8).insert(12).insert(21).insert(31).insert(39).insert(45)
#
#print(bst)
#bst.remove(8)
#bst.remove(19)
#bst.remove(44)
#
##bst.remove(100)
#print(bst)
