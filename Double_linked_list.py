class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __str__(self):
        if not self._length:
            return "[]"
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return "[" + " <-> " .join(values) + "]"
    
    def append(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self._length +=1
        return self

    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            new_node.previous = new_node
            self.head = new_node
        self._length +=1
        return self

    def pop_left(self):
        if not self._length:
            raise Exception("list is empty")
        former_head = self.head
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.head = former_head.next
            former_head.next = None
            self.head.previous = None
        self._length -= 1
        return former_head.value

    def pop_right(self):
        if not self._length:
            raise Exception("list is Empty")
        former_value = self.tail
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.tail = former_tail.previous 
            former_tail.previous = None
            self.tail.next = None
        self._length -=1
        return former_tail.value
    # time complexity O(n)
    # Space complexityO(n)
    def remove(self,value):
        if not self._length:
            raise Exception("list is Empty")
        if self.head.value == value:
            return self.pop_left()
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next
        if current_node.next is None:
            return self.pop_right()
        current_node.next.previous = previous_node
        previous_node.next = current_node.next
        current_node.previous = None
        current_node.next = None
        self._length -=1
        return current_node.value

    def reverse(self):
        if self._length < 2:
            return self
        left_node = None
        middle_node = self.head
        while middle_node is not None:
            right_node = middle_node.next
            middle_node.next = left_node
            left_node = middle_node
            middle_node = right_node 
        self.head, self.tail = self.tail, self.head
        return self

my_list = DoubleLinkedList()
my_list.append(8)
my_list.append(5)

print(my_list)
