class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
class Linkedlist :
    def __init__(self):
        self.head =None
        self.n = 0
        
    def __len__(self):
        return self.n
        
    def insert(self,value):
        new_node =Node(value)
        new_node.next =self.head
        self.head = new_node
            
        self.n=self.n + 1
        
    def __str__(self):
        current =self.head
        result=""
        
        while (current!=None):
            result =result + str(current.data)+ "->"
            current =current.next
        return result[:-2]
    
    def append(self,value):
        new_node=Node(value)
        
        if self.head==None:
            self.head=new_node
            self.n=self.n+1
            return
        
        current =self.head
        while current.next!=None :
            current=current.next
        current.next = new_node
        self.n=self.n+1
        
    def insert_after(self,after,value):
        new_node =Node(value)
        current = self.head
        while current!=None :
            if current.data==after :
                break
            current =current.next
        if current!=None:
            new_node.next = current.next
            current.next = new_node
            self.n=self.n+1
        else:
            return 'item not found !'
        
    def clear(self):
        self.head = None
        self.n = 0
        
    def delete_head(self):
        if self.head==None:
            return 'empty list!'
        self.head = self.head.next
        self.n = self.n -1
        
    def pop(self):
        if self.head ==None:
            return 'empty list'
        
        curr = self.head
        if curr.next==None:
            return self.delete_head()
        while curr.next.next!=None:
            curr = curr.next
        curr.next = None
        self.n = self.n -1
        
    def remove(self,value):
        if self.head==None:
            return "empty list!"
        if self.head.data==value:
            return self.delete_head()
        
        curr = self.head
        while curr.next!=None:
            if curr.next.data==value:
                break
            curr = curr.next
        if curr.next==None:
            return 'element not found'
        else:
            curr.next=curr.next.next
            self.n=self.n -1
    def sum_of_odd_nodes(self):
        temp =self.head
        counter =0
        result =0
        while temp!=None:
            if (counter%2)!=0:
                result =result + temp.data
            counter+=1
            temp =temp.next
        return result
    def create_sentance(self):
        curr = self.head
        while curr!=None:
            if curr.data=="/" or curr.data=="*":
                curr.data=" "
                if curr.next.data=="/" or curr.next.data=="*":
                    curr.next.next.data =curr.next.next.data.upper()  
                    curr.next = curr.next.next             
            curr =curr.next
    def max_num_replace(self,value):
        curr =self.head
        max = curr
        while curr!=None:
            if curr.data>max.data:
                max =curr
            curr = curr.next
        max.data =value

L = Linkedlist()
L.insert(1)
L.append(4)
L.append(5)
L.append(2)
L.append(3)
#L.append("T")
#L.append("h")
#L.append("e")
#L.append("*")
#L.append("/")
#L.append("s")
#L.append("k")
#L.append("y")
#L.append("*")
#L.append("i")
#L.append("s")
#L.append("/")
#L.append("*")
#L.append("b")
#L.append("l")
#L.append("u")
#L.append("e")
#len(L)
#L.insert_after(2,8)
#print(L.insert_after(6,7))
#print(L)
#L.clear()
#for i in range(6):
 #print(L)
 #print(L.delete_head())
#L.pop()
#for i in range(1,6):
 #   print(L.remove(i))
  #  print(L)
#print(L.sum_of_odd_nodes())
#L.create_sentance()
#L.max_num_replace(9)
print(L)
