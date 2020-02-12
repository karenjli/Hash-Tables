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

        index = self._hash_mod(key)

        # Check if the node exist
        if self.storage[index] is None:
            # Just assigned the index above to a newly created Linked Pair
            self.storage[index] = LinkedPair(key, value)
        # if node is not None ==> Collision situation
        else:
            # Save the current value that is being collided
            current = self.storage[index]
            # Check and make sure that value is not none
            while current is not None:
                if current.key == key:
                    # Rewrite the value if key is the same
                    current.value = value
                    break
                else:  # The key is different
                    # Check if next is empty
                    if current.next is None:
                        # Add a value behind if the key is different
                        # By Adding a new pair
                        current.next = LinkedPair(key, value)
                    else:
                        # Reassign the value is next is not None
                        current = current.next

        # Point to the location

    def remove(self, key):
        # Get index
        index = self._hash_mod(key)
        # Point to the current key, value pair as indicated by index
        current = self.storage[index]
        # If current has nothing
        if current is None:
            # Returns message
            return "No key found"
        # Else check if current.next and the key matches
        elif current.next is None and current.key == key:
            # Reset the value to None
            self.storage[index] = None
        else:  # Either there is a next node after current or the key doesn't match
            # set previous node to None
            prevNode = None
            # set the next node to what's after current
            nextNode = current.next

            while current is not None:
                # If the key matches
                if current.key == key:

                    if prevNode is None:
                        # reset the index to the next node
                        self.storage[index] = nextNode
                    else:
                        # this is needed to not delete previous value
                        if nextNode:
                            # reset the next value of the prevNode
                            prevNode.next = nextNode
                        else:
                            # nextNode would be None
                            prevNode.next = None
                    # self.count -= 1
                    break
                else:
                    if current.next is None:
                        return "No key found"
                    else:
                        # Overwrite current value
                        prevNode = current
                        current = current.next
                        nextNode = current.next
                        # self.count -= 1

    def retrieve(self, key):
        # '''
        # Retrieve the value stored with the given key.

        # Returns None if the key is not found.

        # Fill this in.
        # '''
        # Get the index
        index = self._hash_mod(key)
        target = self.storage[index]
        while target is not None:
            if target.key == key:

                return target.value

            else:
                target = target.next
        return None

    def resize(self):
        # '''
        # Doubles the capacity of the hash table and
        # rehash all key/value pairs.

        # Fill this in.
        # '''
        # double the capacity

        self.capacity = self.capacity * 2
        # Set the new storage
        new_storage = [None] * self.capacity

        # Iterate the old list and assign its value to the new one
        for i in range(len(self.storage)):
            current = self.storage[i]

            while current is not None:
                # Create a new index
                index = self._hash_mod(current.key)
                # Check if index is taken
                if new_storage[index] is None:
                    # Assign value to the index in new storage
                    new_storage[index] = LinkedPair(current.key, current.value)
                else:
                    # Assign value to the next since the index is occupied
                    new_storage[index].next = LinkedPair(
                        current.key, current.value)
                current = current.next
        self.storage = new_storage

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
