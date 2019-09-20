class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    # Adds elements to the buffer
    def append(self, item):
        return self.storage.append(item)

    # Returns all of the elements in the buffer in a list in their given order.
    # Should not return any "None" values in the list even if they are present in the buffer
    def get(self):
        items = []
        for item in self.storage:
            print(item)
            if item != None:
                items.append(item)
        return items


buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')
print(buffer.get())
