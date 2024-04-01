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

my_linked_list = LinkedList(9)
my_linked_list.append(15)
# my_linked_list.append(16)
# my_linked_list.append(20)
# my_linked_list.prepend(0)
# my_linked_list.insert(0,15.5)
# my_linked_list.insert(-1,100)
print(my_linked_list)
print(my_linked_list.length)
my_linked_list.traverse()

