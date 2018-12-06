"""Limited size max Binary Heap implementation"""
#!/usr/bin/env python3

class BinaryHeapMax:
    """Heap class implementation"""
    def __init__(self, limit: int = 0):
        self.heap = []
        self.size = 0
        self.max_size = limit
        self.smallest = None

    def perc_up(self, cur_idx):
        """Moving a node up"""
        while (cur_idx - 1) // 2 >= 0:
            # Similar to textbook implementation
            # child = 2p + 1 
            # parent = (child - 1) / 2
            # Compare the current node with its parent node, if current is greater then swap 
            if self.heap[cur_idx] > self.heap[(cur_idx-1) // 2]:
                tmp = self.heap[(cur_idx-1) // 2]
                self.heap[(cur_idx - 1) // 2] = self.heap[cur_idx]
                self.heap[cur_idx] = tmp
            # next current index becomes another child based on the index
            cur_idx = (cur_idx - 1) // 2
        
    def perc_down(self, cur_idx):
        """Moving a node down"""
        while cur_idx * 2 <= self.size:
            # Similar to textbook implementation
            # child = 2p + 1 
            # parent = (child - 1) / 2
            max_child_idx = self.get_max_child(cur_idx)
            if self.heap[cur_idx] < self.heap[max_child_idx]:
                tmp = self.heap[cur_idx]
                self.heap[cur_idx] = self.heap[max_child_idx]
                self.heap[max_child_idx] = tmp
            # next current index becomes another child based on the index
            cur_idx = max_child_idx

    def insert(self, item):
        """Adding a new item"""
        if self.size == 0:
            self.heap.append(item)
            self.size = self.size + 1
        else:
            # If the list is full, rewrite over the smallest node 
            if item >= min(self.heap):
                if self.size == self.max_size:
                    self.heap.remove(min(self.heap))
                    self.size = self.size - 1
                self.heap.append(item)
                self.size = self.size + 1     
                self.perc_up(self.size -1)

    def heapify(self, not_a_heap, show_details=False):
        """Turning a list into a heap"""
        self.heap = [] + not_a_heap[:]
        self.size = len(not_a_heap)
        cur_idx = self.size // 2 - 1
        # Trims down by index and percolates down each of them
        while cur_idx >= 0:
            self.perc_down(cur_idx)
            cur_idx = cur_idx - 1
            if show_details: print(self.heap)
            

    def get_max_child(self, parent_idx):
        """Getting a larger child"""
        # If the index of the right child > size of the heap, right child does not exist 
        # returns left child
        if parent_idx * 2 + 2 > self.size:
            return parent_idx * 2 +1

        else:
            if self.heap[parent_idx*2 + 2] > self.heap[parent_idx*2+1]:
                return parent_idx * 2 + 2    
            else:
                return parent_idx * 2 + 1

    def __len__(self):
        """Get heap size"""
        return self.size

    def __str__(self):
        return str(self.heap)

def main():
    # heap_test = BinaryHeapMax(5)
    # heap_test.insert("A")
    # print(heap_test) # ['A']
    # heap_test.insert("B")
    # print(heap_test) # ['B', 'A']
    # heap_test.insert("C")
    # print(heap_test) # ['C', 'A', 'B']
    # heap_test.insert("D")
    # print(heap_test) # ['D', 'C', 'B', 'A']
    # heap_test.insert("E")
    # print(heap_test) # ['E', 'D', 'B', 'A', 'C']
    # heap_test.insert("F")
    # print(heap_test) # ['F', 'E', 'B', 'C', 'D']
    # heap_test.insert("Z")
    # print(heap_test) # ['Z', 'F', 'C', 'D', 'E']
    # heap_test.insert("H")
    # print(heap_test) # ['Z', 'H', 'D', 'E', 'F']
    # heap_test.insert("Y")
    # print(heap_test) # ['Z', 'Y', 'E', 'F', 'H']
    # heap_test.insert("Z")
    # print(heap_test) # ['Z', 'Z', 'F', 'H', 'Y']

    h1 = BinaryHeapMax()
    h1.heapify([1, 2, 3, 6, 5, 4, 7, 8, 9], show_details=True)

if __name__ == "__main__":
    main()
