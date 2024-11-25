class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        print(len(self.heap))
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        print("parent: ", parent)
        print("index: ", index)
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        biggest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] > self.heap[biggest]:
            biggest = left
        if right < len(self.heap) and self.heap[right] > self.heap[biggest]:
            biggest = right
        if biggest != index:
            self.heap[index], self.heap[biggest] = self.heap[biggest], self.heap[index]
            self._heapify_down(biggest)


heap = MinHeap()
heap.insert(10)
heap.insert(4)
heap.insert(15)
print(heap.heap)

