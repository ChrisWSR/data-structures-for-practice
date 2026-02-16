class MaxBinaryHeap:
    def __init__(self):
        self.items = []
    def insert(self,value):
        self.items.append(value)
        self.move_up()
        return self
    def move_up(self):
        child_idx = len(self.items) -1
        while child_idx > 0:
            parent_idx = (child_idx -1) //2
            if self.items[child_idx] <= self.items[parent_idx]:
                break
            self.swap(child_idx,parent_idx)
            child_idx = parent_idx
    
    def peek(self):
        if not self.items:
            raise Exception("Heap is empty")
        return self.items[0]
    def __str__(self):
        if not self.items:
            return "Empty tree"
        return self._build_tree_string()

    def _build_tree_string(self):
        """Helper method to build tree visualization """
        def print_level(index, prefix, is_tail):
            if index >= len(self.items):
                return ""
            
            result = prefix + ("└── " if is_tail else "├── ") + str(self.items[index]) + "\n"
            
            left_idx = 2 * index + 1
            right_idx = 2 * index + 2
            
            extension = "    " if is_tail else "│   "
            
            # Imprimir hijo derecho primero (aparece arriba visualmente)
            if right_idx < len(self.items):
                result += print_level(right_idx, prefix + extension, False)
            
            # Imprimir hijo izquierdo
            if left_idx < len(self.items):
                result += print_level(left_idx, prefix + extension, True)
            
            return result
        
        return print_level(0, "", True)
    
    def __repr__(self):
        return f"MaxBinaryHeap({self.items})"

    def swap(self,idx_1 ,idx_2):
        self.items[idx_1],self.items[idx_2] = self.items[idx_2],self.items[idx_1]
    def remove_max(self):
        if not self.items:
            raise Exception("Heap its empty")
        max_element = self.items[0]
        end_idx = len(self.items) -1
        self.swap(0,end_idx)
        self.items.pop()
        self.move_down()
        return max_element

    def move_down(self):
        parent_idx = 0
        child_idx = 2 * parent_idx + 1
        end_idx = len(self.items)-1
        while child_idx <= end_idx:
            if child_idx < end_idx and self.items[child_idx] < self.items[child_idx + 1]:
                child_idx += 1
            if self.items[parent_idx] < self.items[child_idx]:
                self.swap(parent_idx, child_idx)
                parent_idx = child_idx
                child_idx = 2 * parent_idx + 1
            else:
                break

#heap = MaxBinaryHeap()
#heap.insert(29).insert(15).insert(44).insert(9).insert(22).insert(40).insert(49)\
#   .insert(5).insert(10).insert(19).insert(27).insert(35).insert(46).insert(58)\
#   .insert(8).insert(12).insert(21).insert(31).insert(39).insert(45).insert(2)
#print(heap)

Heap = MaxBinaryHeap()
#values = [10,27,24,40,35,19,15]
#for a in values:
#    Heap.insert(a)
#print(Heap)
values = [40,27,35,10,24,19,15]
for a in values:
    Heap.insert(a)
print(Heap)
print("remove max element",Heap.remove_max())

print(Heap)
array = [23,44,11,27,54,35,13,61,22,48,41,39,52,17,65]
def move_down_heapify(array,start_idx, end_idx):
    child_idx = 2 * start_idx + 1
    while child_idx <= end_idx:
        if child_idx < end_idx and array[child_idx] < array[child_idx + 1]:
            child_idx += 1
        if array[start_idx] < array[child_idx]:
            array[start_idx], array[child_idx] = array[child_idx],array[start_idx]
            start_idx = child_idx
            child_idx = 2 * start_idx + 1
        else:
            break
    return array

def heapify(array):
    last_parent_idx = len(array) //2 - 1
    for idx in range(last_parent_idx,-1,-1):
        move_down_heapify(array,idx,len(array)-1)
    return array

array1=heapify(array)
print(array1)
