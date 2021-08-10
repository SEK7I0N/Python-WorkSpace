class Node:
    """Node Class"""

    def __init__(self, data=None, next=None):
        """__init__ constructor

        Args:
            data (unspecified, optional): stores node value. Defaults to None.
            next (Node, optional): links to the next node. Defaults to None.
        """
        self.data = data
        self.next = next

    def display_node(self):
        """display_node displays the node data
        """
        print(self.data)


class LinkedList:
    """Linked List Class"""

    def __init__(self, data=None):
        """__init__ constructor

        Args:
            data (unspecified, optional): value which is stored in a node. Defaults to None.
        """
        self.head = Node(data)
        self.tail = self.head
        if data is None:
            self.length = 0
        else:
            self.length = 1

    def append(self, data):
        """append adds a node at the end of linked list

        Args:
            data (unspecified): value which is stored in a node
        """
        new_node = Node(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def prepend(self, data):
        """prepend adds a  node at the start of the linked list

        Args:
            data (unspecified): value which is stored in the node
        """
        new_node = Node(data, self.head)
        self.head = new_node
        self.length += 1

    def display_list(self):
        """display_list displays linked list
        """
        temp = self.head
        output = ''
        while temp.next:
            output += '{} --> '.format(temp.data)
            temp = temp.next
        output += '{} --> None'.format(temp.data)
        print(output, '\n')

    def display_properties(self):
        """display_properties displays the values of head, tail and length
        """
        print("Properties:")
        print("\tHead Data: {}".format(
            self.head.data))
        print("\tTail Data: {}".format(
            self.tail.data))
        print("\tLength: {}".format(
            self.length))

    def insert(self, index, data):
        """insert adds the data at the specified index in the list

        Args:
            index (int): index of the data to be inserted at
            data (unspecified): value which is stored in the node
        """
        new_node = Node(data)
        if index is 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            pass
        elif index < self.length:
            iterator = 1
            temp = self.head
            while iterator < index:
                temp = temp.next
                print('Temp Data ====>', temp.data)
                iterator += 1
            new_node.next = temp.next
            print('NEW Nde Data ====>', new_node.data)
            temp.next = new_node
            print(
                f'Data inserted at the index {index} of the linked list')
            self.length += 1
            pass

        else:
            self.tail.next = new_node
            self.tail = new_node
            print(
                f'Data inserted at the end of the list as index {index} was greater than length {self.length} of the linked list')
            self.length += 1
        pass


lst = LinkedList(10)
lst.append(5)
lst.prepend(16)
lst.prepend('abc')
lst.display_list()

lst.insert(0, 'this')
lst.display_list()

lst.insert(123, 'yuiagsd5623')
lst.display_list()

lst.insert(6, 22/7)
lst.display_list()
lst .display_properties()
