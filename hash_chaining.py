class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


class LL:

  def __init__(self):
    self.head = None

  def add(self, key, value):

    new_node = Node(key, value)

    if self.head == None:
      self.head = new_node
    else:

      temp = self.head

      while temp.next != None:
        temp = temp.next

      temp.next = new_node

  def delete_head(self):

    if self.head == None:
      return "Empty"
    else:
      self.head = self.head.next

  def remove(self, key):
    if self.head.key == key:
      self.delete_head()
      return 

    if self.head == None:
      return "Empty"
    else:

      temp = self.head

      while temp.next != None:
        if temp.next.key == key:
          break
        temp = temp.next

      if temp.next == None:
        return "Not Found"
      else:
        temp.next = temp.next.next
        

  def traverse(self):

    temp = self.head

    while temp != None:

      print(temp.key,"-->",temp.value," ", end=" ")
      temp = temp.next

  def size(self):

    temp = self.head
    counter = 0

    while temp != None:

      counter += 1
      temp = temp.next

    return counter

  def search(self,key):

    temp = self.head
    pos = 0

    while temp != None:

      if temp.key == key:
        return pos

      temp = temp.next
      pos += 1

    return -1

  def get_node_at_index(self,index):

    temp = self.head
    counter = 0

    while temp is not None:

      if counter == index:
        return temp
      temp = temp.next
      counter+=1

class Dictionary :
    def __init__(self,capacity):
      self.capacity =capacity
      self.size =0
      
      self.buckets = self.make_array(self.capacity)
      
    def make_array(self,capacity):
        l=[]
        for i in range(capacity):
            l.append(LL())
        return l
      
    def __str__(self):
      for i in self.buckets:
        i.traverse()
      return " "
    
    def put(self,key,value):
      bucket_index = self.hash_function(key)
      node_index = self.get_node_index(bucket_index,key)
      if node_index==-1:
        self.buckets[bucket_index].add(key,value)
        self.size+=1
        load_factor = self.size/self.capacity
        print(load_factor)
        if load_factor>=2:
          self.rehash()
      else:
        node =self.buckets[bucket_index].get_node_at_index(node_index)
        node.value =value
        
    def get(self,key):
      bucket_index = self.hash_function(key)
      res = self.buckets[bucket_index].search(key)
      
      if res==-1:
        return ("not found")
      else:
        node =self.buckets[bucket_index].get_node_at_index(res)
        return node.value
      
    def rehash(self):
      self.capacity=self.capacity*2
      oldbucket = self.buckets
      self.size = 0
      self.buckets =self.make_array(self.capacity)
      for i in oldbucket:
        for j in range(i.size()):
          node =i.get_node_at_index(j)
          keyitem = node.key
          valueitem = node.value
          self.put(keyitem,valueitem)
          
    def deletekey(self,key):
      bucket_index = self.hash_function(key)
      self.buckets[bucket_index].remove(key)  
      
    def get_node_index(self,bucket_index,key):
      node_index= self.buckets[bucket_index].search(key)
      return node_index
    
    def hash_function(self,key):
        return abs(hash(key))%self.capacity
      
      
d = Dictionary(2)
d.put("python",45)
d.put("java",34)
d.put("php",56)

print(d.get("java"))