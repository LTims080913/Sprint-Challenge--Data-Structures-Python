class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            # print(str(len(self.storage))+">"+str(self.capacity))
            self.storage.append(item)
        else:
            # print(f"{item}, {self.oldest}")
            self.storage.pop(self.oldest)
            self.storage.insert(self.oldest, item)
            if self.oldest == len(self.storage)-1:
                self.oldest = 0
            else:
                self.oldest +=1
        
    def get(self):
        return self.storage

