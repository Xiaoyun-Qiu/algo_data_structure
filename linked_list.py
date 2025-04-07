class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def empty(self):
        return self.head is None
    def __len__(self):
        return self.size

    def prepend(self,x):
        if self.empty():
            self.head = Node(x)
            self.tail = self.head
        else:
            p = self.head
            new_node = Node(x)
            new_node.next = p
            self.head = new_node
        self.size += 1

    def append(self, x):
        if self.empty():
            self.head = Node(x)
            self.tail = self.head
        else:
            last_node = self.tail
            current = Node(x)
            last_node.next = current
            self.tail = current
        self.size += 1

    def insert(self, idx, x):
        if self.size < idx +1:
            return None
        elif idx ==0:
            self.prepend(x)
        else:
            current = self.head
            new_node = Node(x)
            count = 0
            while count<idx-1:
                current = current.next
                count += 1
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def pop(self):
        if self.empty():
            return None
        elif self.size == 1:
            x = self.head.data
            self.head = None
            return x
        else:
            current = self.head
            count = 0
            while count < self.size-2:
                current = current.next
                count += 1
            self.tail = current
            x = current.next.data
            current.next = None
            self.size -= 1
            return x

    def __getitem__(self,idx):
        if self.size<idx+1:
            print("Out of range")
            return None
        else:
            current = self.head
            for _ in range(idx):
                current = current.next
            print(current.data)
            return current.data

    def remove(self,idx):
        if self.size<idx+1:
            print('Out of range')
            return None
        elif idx == self.size -1:
            self.pop()
        else:
            current = self.head
            for _ in range(idx):
                current = current.next
            current.data = current.next.data
            current.next = current.next.next
            self.size -= 1

    def index(self,x):
        count = 0
        found = False
        current = self.head
        while current.data is not None and not found:
            if current.data == x:
                found = True
                print(count)
                return count
            else:
                current = current.next
                count += 1
        return None

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print("")



if __name__ == '__main__':
    l = LinkedList()
    l.prepend(3)
    l.prepend(2)

    l.append(4)
    print(l.pop())
    l.append(5)
    l.insert(0,1)
    l.printList()

    l.remove(4)
    l.printList()
    l[0]
    l.index(3)












