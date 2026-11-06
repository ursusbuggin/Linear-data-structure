"""
Assessment 3.2: Linear Data Structure
Program 4: Singly Linked List

A dynamic, menu-driven program. Each element is a Node that holds a value and
a reference to the next node. The list grows and shrinks while the program runs.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # reference to the next node (None means end of list)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        """Add a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at_tail(self, data):
        """Add a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def insert_at_position(self, data, position):
        """Add a new node so that it ends up at the given index."""
        if position < 0 or position > self.length:
            return False
        if position == 0:
            self.insert_at_head(data)
            return True
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        return True

    def delete_value(self, data):
        """Remove the first node holding the given value."""
        if self.head is None:
            return False
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return True
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.length -= 1
                return True
            current = current.next
        return False

    def delete_first(self):
        """Remove the first node (the 'DELETE FIRST NODE' step in the algorithm).
        Returns the removed value, or None if the list is empty."""
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next
        self.length -= 1
        return removed

    def search(self, data):
        """Return the index of the first match, or -1 if not found."""
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        """Print the list from head to tail."""
        if self.head is None:
            print("The linked list is empty.")
            return
        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        print("HEAD -> " + " -> ".join(parts) + " -> None")
        print(f"Length: {self.length}")


def main():
    linked_list = LinkedList()
    while True:
        print("\n===== LINKED LIST OPERATIONS =====")
        print("1. Insert at head")
        print("2. Insert at tail")
        print("3. Insert at a position")
        print("4. Delete first node")
        print("5. Delete by value")
        print("6. Search for a value")
        print("7. Display list")
        print("8. Show length")
        print("9. Exit")
        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            value = input("Enter the value to insert at the head: ")
            linked_list.insert_at_head(value)
            print(f"'{value}' was added at the head.")
        elif choice == "2":
            value = input("Enter the value to insert at the tail: ")
            linked_list.insert_at_tail(value)
            print(f"'{value}' was added at the tail.")
        elif choice == "3":
            value = input("Enter the value to insert: ")
            try:
                position = int(input(f"Enter the position (0 to {linked_list.length}): "))
            except ValueError:
                print("Invalid position. Please enter a whole number.")
                continue
            if linked_list.insert_at_position(value, position):
                print(f"'{value}' was inserted at position {position}.")
            else:
                print("Position is out of range.")
        elif choice == "4":
            removed = linked_list.delete_first()
            if removed is None:
                print("The linked list is empty. Nothing to delete.")
            else:
                print(f"The first node '{removed}' was deleted.")
        elif choice == "5":
            value = input("Enter the value to delete: ")
            if linked_list.delete_value(value):
                print(f"'{value}' was deleted.")
            else:
                print(f"'{value}' was not found (or the list is empty).")
        elif choice == "6":
            value = input("Enter the value to search for: ")
            index = linked_list.search(value)
            if index == -1:
                print(f"'{value}' was not found.")
            else:
                print(f"'{value}' was found at index {index}.")
        elif choice == "7":
            linked_list.display()
        elif choice == "8":
            print(f"The linked list has {linked_list.length} node(s).")
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 9.")


if __name__ == "__main__":
    main()
