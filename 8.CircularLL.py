class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class CSLL:
    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0
    def __init__(self,value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        temp = self.head
        res = ""
        while temp:
            res +=  str(temp.val)
            temp = temp.next
            if temp == self.head:
                break
            res += "->"
        return res

    def append(self,value):
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            self.head,self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

        

csll = CSLL(10)
csll.append(100)
csll.append(200)
print(csll)