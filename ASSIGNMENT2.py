class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def show(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, position):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        if position < 1:
            print("Position should be 1 or more.")
            return
        if position == 1:
            print(f"Deleting the first node which is {self.head.data}")
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 1
        while current and count < position:
            prev = current
            current = current.next
            count += 1
        if current is None:
            print(f"Position {position} is out of range.")
            return
        print(f"Deleting node at position {position} which is {current.data}")
        prev.next = current.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

if __name__ == "__main__":
    print("Linked List Assignment 2")

    my_list = LinkedList()

    print("\nAdding numbers to the list:")
    for number in [10, 20, 30, 40, 50]:
        my_list.add(number)
        my_list.show()

    print("\n deleting some nodes:")

    my_list.delete(3)
    my_list.show()

    my_list.delete(1)
    my_list.show()

    my_list.delete(10)
    my_list.show()

    my_list.delete(1)
    my_list.delete(1)
    my_list.delete(1)
    my_list.delete(1)

    print("\nFinal list:")
    my_list.show()
    print(f"List has {my_list.size()} node(s).")
