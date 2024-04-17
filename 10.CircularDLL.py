class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # def __init__(self,value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     new_node.next = new_node
    #     new_node.prev = new_node
    #     self.length = 1

    def __str__(self):
        res = ""
        temp = self.head
        while temp:
            res += str(temp.value)
            temp = temp.next
            if temp is self.head:
                break
            res += "<->"
        return res

    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def prepend(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp is self.head:
                break
cdll = CDLL()
cdll.append(100)
cdll.append(200)
cdll.prepend(50)
print(cdll)
cdll.traverse()



