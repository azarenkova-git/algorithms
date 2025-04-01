class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_front(self, data):
        # создаём новый узел
        # и добавляем в него новое значение data
        new_node = Node(data)
        if self.head is None:
            # если ранее список был пуст, значит новый элемент
            # и будет являться головой (head)
            self.head = new_node
            return
        # если список не пуст, то устанавливаем head
        # в качестве параметра next для нового узла
        new_node.next = self.head
        # записываем в head новый узел
        self.head = new_node

    def insert_after(head, key, new_data):
        curr = head

        # Iterate over Linked List to find the key
        while curr is not None:
            if curr.data == key:
                break
            curr = curr.next

        # if curr becomes None means, given key is not
        # found in linked list
        if curr is None:
            print("Node not found")
            # Return the head of the original linked list
            return head

        # Allocate new node and make the element to be inserted
        # as a new node
        new_node = Node(new_data)

        # Set the next pointer of new node to the next pointer of given node
        new_node.next = curr.next

        # Change the next pointer of given node to the new node
        curr.next = new_node

        # Return the head of the modified linked list
        return head
