class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SiglyLinkedList:
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
        return "[" + " -> " .join(values) + "]"

    def append(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length +=1
        return self

    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length +=1
        return self
     
    def pop_left(self):
        if not self._length:
            raise Exception("list is empty")
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self._length -= 1
        if not self._length:
            self.tail = None
        return former_head.value

    def pop_right(self):
        if not self._length:
            raise Exception("list is Empty")
        tail_value = self.tail.value
        if self._length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self._length -=1
        return tail_value
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
            self.tail = previous_node
        previous_node.next = current_node.next
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
     

my_list = SiglyLinkedList()

my_list.append(3)
my_list.append(2)
my_list.append(1)
my_list.prepend(2)
print("my list",my_list)
print(my_list.head.value)
print("head :",my_list.head)
print(my_list.tail.value)
print(my_list._length)
my_list.pop_left()
print(my_list._length)
my_list.reverse()
print("my list",my_list)
