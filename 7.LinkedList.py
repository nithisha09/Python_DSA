class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        result = ""
        temp=self.head
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += "->"
            temp=temp.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def insert(self,index,value):
        new_node = Node(value)
        if index<0 or index>self.length:
            return False
        elif self.length == 0:
            self.head = self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length+=1
        return True
    
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def search(self,x):
        temp = self.head
        count = 0
        while temp:
            if temp.value == x:
                return count
            temp = temp.next
            count += 1
        return -1
    
    def get(self,index):
        if index<0 or index>=self.length:
            return -1
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.value
        
    def set(self,index,val):
        if index<0 or index>=self.length:
            return False
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = val
            return True
        # we can also use get method within this class
    
    def pop_first(self):
        if self.head:
            if self.length == 1:
                self.head = self.tail = None
            else:
                pop = self.head
                self.head = self.head.next
                pop.next = None
            self.length -= 1
            return True
        return False
    
    def pop(self):
        if self.head:
            if self.length == 1:
                self.head = self.tail = None
            else:
                temp = self.head
                # while temp.next.next:
                while temp.next.next is not None:
                    temp = temp.next
                self.tail = temp
                self.tail.next = None
            self.length -= 1
            return True
        return False
    
    def remove(self,index):
        if index<=0 or index>=self.length or index == self.length-1:
            return False
            # can use pop_first/pop method
        if self.head:
            if self.length == 1:
                self.head = self.tail = None
            else:
                temp = self.head
                for _ in range(index-1):
                    temp = temp.next
                pop = temp.next
                temp.next = temp.next.next
                pop.next = None
            self.length -= 1
            return True
        return False
    # Can use get method

    def delete_all(self):
        self.head = self.tail = None
        self.length = 0
        
my_linked_list = LinkedList(9)
my_linked_list.append(15)
my_linked_list.append(16)
my_linked_list.append(20)
my_linked_list.prepend(0)
# my_linked_list.insert(0,15.5)
# my_linked_list.insert(-1,100)
# print(my_linked_list.length)
# my_linked_list.traverse()
# print(my_linked_list.search(20))
# print(my_linked_list.get(-3))
# print(my_linked_list.set(0,100))
# print(my_linked_list.pop_first())
print(my_linked_list.pop())
# print(my_linked_list.remove(4))
# my_linked_list.delete_all()
print(my_linked_list)
