# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        # '''
        # Hash an arbitrary key and return an integer.

        # You may replace the Python hash with DJB2 as a stretch goal.
        # '''

        return hash(key)

    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash

    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''

        return self._hash(key) % self.capacity

    def insert(self, key, value):
        # '''
        # Store the value with the given key.

        # Hash collisions should be handled with Linked List Chaining.

        # Fill this in.
        # '''
        # Define index as a hashed key
        index = self._hash(key)
        # Point to the location of the specified index
        node = self.storage[index]
        # Check if the node exist
        if node is None:
            # Just assigned the index above to a newly created Linked Pair
            self.storage[index] = LinkedPair(key, value)

        # if node is not None ==> Collision situation

    def remove(self, key):
        # '''
        # Remove the value stored with the given key.

        # Print a warning if the key is not found.

        # Fill this in.
        # '''
        # Look for the index
        index = self._hash(key)
        # Point to the location
        node = self.storage[index]
        # Check to see the node actually exists
        while node is not None and node.key != key:
            # Define Prev as Node??
            prev = node
            # Overwrite the node to be deleted with its next one
            node = node.next
        # Goes through the whole loop and found nothing
        if node is None:
            return None
        # That means something was found
        else:
            # Define result
            result = node.value
            # Same procedure as removing from Linked List
            if prev is None:
                node = None
            else:
                # prev.next is basically node, which now equals to node.next
                # which is the value after original node
                prev.next = prev.next.next
            # since result = node.value, and node is overwritten
            # result now has the new value
            return result

    def retrieve(self, key):
        # '''
        # Retrieve the value stored with the given key.

        # Returns None if the key is not found.

        # Fill this in.
        # '''
        # Get the index
        index = self._hash(key)
        # Point to the specific location
        node = self.storage[index]
        # Check if the node exists
        if node is None:
            return None
        else:
            # Return value if the node exists
            return node.value

    def resize(self):
        # '''
        # Doubles the capacity of the hash table and
        # rehash all key/value pairs.

        # Fill this in.
        # '''
        # double the capacity
        self.capacity *= 2
        # Set the new storage
        new_storage = [None] * self.capacity
        # Iterate the old list and assign its value to the new one
        for i in self.storage:
            new_storage[i] = self.storage[i]


# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)
#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")
#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))
#     print("")
key = "123456"
H = HashTable(3)
print(H._hash(key))
