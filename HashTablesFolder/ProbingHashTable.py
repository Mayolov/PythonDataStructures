class ProbingHashTable:
    def __init__(self, max_size=4096):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size
     
    
    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key,value
    
    
    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]
    
    
    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key,value

    
    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]
    

def get_index(data_list, a_string):
    # stores result 
    result = 0
    
    for a_character in a_string:
        # Convert the character to a number
        a_number = ord(a_character)
        #update result by adding the number
        result += a_number
        
    list_index = result % len(data_list)
    
    # Ensure that the index is within the bounds of the list
    if list_index < 0 or list_index >= len(data_list):
        list_index = 0
        
    return list_index
    
def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list,key)

    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        
        # If it is None, return the index
        if kv is None:
            return idx
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if k==key:
            return idx
        
        # Move to the next index
        idx += 1
        
        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0