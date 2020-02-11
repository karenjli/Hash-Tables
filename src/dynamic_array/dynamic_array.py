class DynamicArray:
    def __init__(self, capacity=8):
        self.count=0
        self.capacity=capacity
        self.storage=[None] * self.capacity
        
    def insert(self, index, value):
        if index >= self.count:
            # TODO: better error handling
            print ("Error: Index out of bounds")
            self.storage[self.count] = value
            self.count +=1
            
    def double_size(self):
        self.capacity *=2
        new_storage = [None] * self.capacity
        
        for i in range (self.count):
            new.storage[i] = self.storage[i]