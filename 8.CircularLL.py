class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    # def __init__(self,value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

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
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1

    def insert(self,value,index):
        if index<0 or index>self.length:
            return False
        elif not self.head:
            self.prepend(value)
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
        return True
    
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
            if temp is self.head:
                break
    
    def search(self,x):
        temp = self.head
        index = 0
        while temp:
            if temp.val == x:
                return index
            temp = temp.next
            index += 1
            if temp == self.head:
                return -1
    
    def get(self,index):
        if index<0 or index>=self.length:
            return -1
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.val
        
    def set(self,index,new_val):
        if index<0 or index>=self.length:
            return False
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.val = new_val
            return True
    
    def pop_first(self):
        if not self.head:
            return None
        else:
            if self.length == 1:
                pop_node = self.head
                self.head = None
                self.tail = None
            else:
                pop_node = self.head
                self.head = pop_node.next
                self.tail.next = self.head
        pop_node.next = None
        self.length -= 1
        return pop_node.val

    def pop(self):
        if not self.head:
            return None
        elif self.length == 1:
            pop_node = self.tail
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            pop_node = temp.next
            temp.next = self.head
        pop_node.next = None
        self.length -= 1
        return pop_node.val
    
    def remove(self,index):
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        elif index<0 or index>=self.length:
            return None
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            node_removed = temp.next
            temp.next = node_removed.next
            node_removed.next = None
            self.length -= 1
            return node_removed.val
    
    def delete_all(self):
        self.tail.next = None
        self.head = self.tail = None
        self.length = 0

    def delete_by_value(self, value):
        if not self.head:
            return False
        temp = self.head
        if temp.value == value and self.head == self.tail:
                self.head = self.tail = None
                self.length -= 1
                return True
        elif temp.value == value:
                del_node = self.head
                self.head = del_node.next
                self.tail.next = self.head
                del_node.next = None
                self.length -= 1
                return True
        while temp:
            # print(temp.value)
            if temp.next.value == value:
                if temp.next == self.tail:
                    del_node = temp.next
                    temp.next = del_node.next
                    del_node.next = None
                    self.tail = temp
                else:
                    del_node = temp.next
                    temp.next = del_node.next
                    del_node.next = None
                self.length -= 1
                return True
            temp = temp.next
            if temp.next is self.head:
                return False
csll = CSLL()
csll.append(10)
csll.append(11)
csll.append(12)
csll.prepend(9)
csll.insert(13,4)
csll.insert(8,0)
csll.insert(10.5,3)
print(csll)
# csll.traverse()
# print(csll.search(12))
# print(csll.get(4))
# print(csll.set(5,11.5))
# print(csll.set(6,12))
# print(csll.pop_first())
# print(csll.pop())
# print(csll.remove(3))
csll.delete_all()
print(csll)