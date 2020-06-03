
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'HashTableEntry({repr(self.key)}, {repr(self.value)})'



# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.size = 0
        # self.buckets = [None] * self.capacity
        self.buckets = [None for i in range(capacity)]
        self.head = None


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        print("this is the len of the array", len(self.buckets))
        return len(self.buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        print(len(self.buckets))
        return len(self.buckets)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        byte_array = str(key).encode("utf-8")
        for x in byte_array:
            hash = (( hash * 33) ^ x) % 0x100000000
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        new_node = HashTableEntry(key, value)
        current_node = self.buckets[bucket_index]

        if current_node:
            head_node = None
            while current_node:
                if current_node.key == key:
                    # found existing key, replace value
                    current_node.value = value
                    return
                head_node = current_node
                current_node = current_node.next
            # if we get this far, we didn't find an existing key
            # so just append the new node to the end of the bucket
            head_node.next = new_node
            self.size += 1 
        else:
            self.buckets[bucket_index] = new_node
            self.size += 1   


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = self.buckets[index]
        prev = None
        # While node exists and keys do not match, step through the LL
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # If node does not exist, let them know that key was not found
        if node is None:
            print('Warning, key not found!')
        # Otherwise, if node exists with no other conditions required...
        else:
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = node.next
        self.size -= 1

       

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # slot = self.hash_index(key)
        # return self.buckets[slot]
        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        current_node = self.buckets[bucket_index]
        if current_node:
            while current_node:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next

        return None
    
    
    

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
         # Need logic here to double the size of the hashtable and rehash the elements to the new table
        # Get old hashtable
        old_hash_table = self.buckets
        # Define new hashtable capacity
        self.capacity = new_capacity
        # Generate a new hashtable with the updated capacity
        new_hash_table = [None] * new_capacity
        # Assign that new hashtable to storage
        self.buckets = new_hash_table
        # Loop over the old hash table checking for values, if they exist....rehash and add them back in.
        for v in old_hash_table:
            if v is not None:
                while v is not None:
                    self.put(v.key, v.value)
                    v = v.next
        
        

#[[('line_4', 'And the mome raths outgrabe.')], [('line_5', '"Beware the Jabberwock, my son!')], [('line_6', 'The jaws that bite, the claws that catch!')], [('line_7', 'Beware the Jubjub bird, and shun')], [('line_8', 'The frumious Bandersnatch!'), ('line_11', 'So rested he by the Tumtum tree')], [('line_1', "'Twas brillig, and the slithy toves"), ('line_9', 'He took his vorpal sword in hand;'), ('line_10', 'Long time the manxome foe he sought--')], [('line_2', 'Did gyre and gimble in the wabe:')], [('line_3', 'All mimsy were the borogoves,'), ('line_12', 'And stood awhile in thought.')]]


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", "The frumious Bandersnatch!")
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
