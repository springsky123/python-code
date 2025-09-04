# Create a node class to create a node

class node:
        def __init__(self,data):
                self.data = data
                self.next = None

# Create a linketlist class

class linkedlist:
        def __init__(self):
                self.head = None
        # method to add a node at the beginning of the LL
        def insertAtBegin(self,data):
                new_node = node(data)
                new_node.next = self.head
                self.head  = new_node
        # method to add a node at any index
        def insertAtIndex(self,data,index):
                if index == 0:
                        self.insertAtBegin(data)
                        return
                position = 0
                current_node = self.head
                while current_node is not None and position+1 !=index:
                        position+=1
                        current_node = current_node.next
                if current_node is not None:
                        new_node = node(data)
                        new_node.next = current_node.next
                        current_node.next = new_node
                else:
                        print("Index not present")
        # method to  add a node at the end of LL
        def insertAtEnd(self,data):
                new_node = node(data)
                if self.head is None:
                        self.head = new_node
                        return
                current_node = self.head
                while current_node.next:
                        current_node = current_node.next
                current_node.next = new_node
        # update node at a given position
        def updatenode(self,val,index):
                current_node = self.head
                position = 0
                while current_node is not None and position != index:
                        position +=1
                        current_node = current_node.next
                if current_node is not None:
                        current_node.data = val
                else:
                        print("Index not present")
        # method to remove first node of linkedlist
        def remove_first_node(self):
                if self.head is None:
                        return
                self.head = self.head.next
        # methos to remove last node of linked list
        def remove_last_node(self):
                if self.head is None:
                        return
                # if there's only one node
                if self.head.next is None:
                        self.head = None
                        return
                # Traverse to the second last node
                current_node = self.head
                while current_node.next and current_node.next.next:
                        current_node = current_node.next
                current_node.next = None
        # method to remove a node at a given index
        def remove_at_index(self,index):
                if self.head is None:
                        return
                if index == 0:
                        self.remove_first_node()
                        return
                current_node = self.head
                position = 0
                while current_node is not None and current_node.next is not None and position+1 != index:
                        position+=1
                        current_node = current_node.next
                if current_node is not None and current_node.next  is not None:
                        current_node.next = current_node.next.next
                else:
                        print("Index not present")
        # method to remove a node from the linked list by its data
        def remove_node(self,data):
                current_node = self.head
                # if the node to be removed is the head node
                if current_node is not None and current_node.data == data:
                        self.remove_first_node()
                        return
                # traverse and find the node with the matching data
                while current_node is not None and current_node.next is not None:
                        if current_node.next.data == data:
                                current_node.next = current_node.next.next
                                return
                        current_node = current_node.next
                # if the data was not found
                print("Node with the given data not found")
        # print the size of the linked list
        def sizeofLL(self):
                size = 0
                current_node = self.head
                while current_node:
                        size+=1
                        current_node = current_node.next
                return size
        # print the linked list
        def printLL(self):
                current_node = self.head
                while current_node:
                        print(current_node.data)
                        current_node = current_node.next
# create a new linked list
Llist = linkedlist()
# add nodes to the linked list
Llist.insertAtEnd("A")
Llist.insertAtEnd("B")
Llist.insertAtBegin("C")
Llist.insertAtEnd("D")
Llist.insertAtIndex("E",2)
#print the linkedlist
print("Node data:")
Llist.printLL()

# remove nodes
print("\n Remove first node:")
Llist.remove_first_node()
Llist.printLL()

print("\n Remove last node:")
Llist.remove_last_node()
Llist.printLL()

print("\n Remove node at index 1:")
Llist.remove_at_index(1)
Llist.printLL()

# print the linked list after all removals

print("\n Linked list after removing a node:")
Llist.printLL()

