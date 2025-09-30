class Dictionary:
    def __init__(self,size):
        self.size =size
        self.slot =[None]*self.size
        self.data =[None]*self.size
        
    def put(self,key,value):
        hash_value =self.hash_function(key)
        if self.slot[hash_value]==None:
            self.slot[hash_value]=key
            self.data[hash_value]=value
        else:
            if self.slot[hash_value]==key:
                self.data[hash_value] =value
            else:
                new_hash_value =self.rehash(hash_value)
                while self.slot[new_hash_value]!=None and self.slot[new_hash_value]!=key:
                    new_hash_value =self.rehash(new_hash_value)
                
                if self.slot[new_hash_value]==None:
                    self.slot[new_hash_value] =key
                    self.data[new_hash_value] =value
                else:
                    self.data[new_hash_value]= value
    
    def get(self,key):
        start_pos =self.hash_function(key)
        curr_pos =start_pos
        while self.slot[curr_pos]!=None:
            if self.slot[curr_pos]==key:
                return self.data[curr_pos]
            curr_pos =self.rehash(curr_pos)
            if self.slot[curr_pos]== start_pos:
                return 'not found'
        return 'key not found'
    
    def __setitem__(self,key,value):
        self.put(key,value)            
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __str__(self):
        for i in range(len(self.slot)):
            if self.slot[i]!= None:
                print(self.slot[i] ,":",self.data[i],end=' ')
        return " "
    
    
    
    def delete(self,key):
        start_pos =self.hash_function(key)
        curr =start_pos
        while self.slot[curr] is not None:
            if self.slot[curr]==key:
                self.slot[curr]=None
                self.data[curr]=None
                return key
            curr =self.rehash(curr)
            if self.slot[curr]==start_pos:
                break
        return  print("key not found")    
        
    def hash_function(self,key):
        return  sum(ord(ch) for ch in key) % self.size    #abs(hash(key))%self.size
    
    def rehash(self,old_hash_value):
       return (old_hash_value + 1)%self.size 
    
    
h =Dictionary(3)
#print(hash("python"))
#h.put("python",45)
#h.put("java",23)
#h.put("php",50)
#print(h.slot)
#print(h.data)

h['python']=45
h['java']=40
h['c']=5
print(h)
print(h.get('python'))
print(h["java"])
h["python"]=50

print(h.delete("c"))
print(h)