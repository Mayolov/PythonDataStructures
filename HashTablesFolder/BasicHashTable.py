class BasicHashTable:
    def __init__(self, max_size = 4096):
        self.data_list = [None] * max_size
        
    def insert(self,key,value):
        idx = get_index(self.data_list, key)
        
        self.data_list[idx] = key, value
        
    
    def find(self,key):
        
        idx = get_valid_index(self.data_list, key)
        
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key,value = kv
            return value
    
    def update(self, key, value):
        idx = get_index(self.data_list,key)
        self.data_list[idx] = key,value
    
    def list_all(self):
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
    
    return list_index
        
def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list,key)
    
    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        
        # If it is None, return the index
        if kv[0]:
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
    
