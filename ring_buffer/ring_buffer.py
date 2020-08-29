class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        elif len(self.data) == self.capacity:
            self.data[self.current] = item
            self.current = (self.current + 1) % self.capacity   

    def get(self):
        return self.data