# linked list

#  node object
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


#  Linkedlist class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.head = node
        self.count += 1

    def lookup(self, value):
        node = self.head
        while node != None:
            if node.get_value() == value:
                return node.get_value()
            node = node.get_next()
        return None

    def dump_list(self):
        node = self.head
        while node != None:
            print("Node: ", node.get_value())
            node = node.get_next()


itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)

itemlist.dump_list()

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.lookup(13))
print("Finding item: ", itemlist.lookup(78))
