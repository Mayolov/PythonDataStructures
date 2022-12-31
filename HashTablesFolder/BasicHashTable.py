class BasicHashTable:
    def __init__(self,max_size = 1024):
        self.data_list = [None] * max_size
        
    def insert(self,key,value):
        idx = self.get_index(key)
        
        self.data_list[idx] = key, value
        
    
    def find(self,key):
        
        idx = self.get_index(key)
        
        kv = self.data_list[idx]
        if kv is None:
            return None
        else:
            key,value = kv
            return value
    
    def update(self, key, value):
        idx = self.get_index(key)
        self.data_list[idx] = key,value
    
    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]


    def get_index(self, a_string):
        # stores result
        result = 0
        
        for a_character in a_string:
            # Convert the character to a number
            a_number = ord(a_character)
            #update result by adding the number
            result += a_number
            
        list_index = result % len(self.data_list)
        
        return list_index
            
    
