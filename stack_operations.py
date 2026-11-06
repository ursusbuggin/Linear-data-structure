"""
Assessment 3.2: Linear Data Structure
Program 2: Stack (LIFO - Last In, First Out)

A dynamic, menu-driven program. The user pushes and pops values while the
program runs. The last item pushed is always the first one popped.
"""


class Stack:
    def __init__(self):
        self.items = []  # the end of the list is the "top" of the stack

    def is_empty(self):
        return len(self.items) == 0

    def push(self, value):
        """Place a value on top of the stack."""
        self.items.append(value)

    def pop(self):
        """Remove and return the top value. Returns None if empty."""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Look at the top value without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        """Show the stack from top to bottom."""
        if self.is_empty():
            print("The stack is empty.")
            return
        print("Stack (top to bottom):")
        for position, value in enumerate(reversed(self.items)):
            label = "  <- TOP" if position == 0 else ""
            print(f"  | {value} |{label}")
        print("  +-----+")


def main():
    stack = Stack()
    while True:
        print("\n===== STACK OPERATIONS (LIFO) =====")
        print("1. Push")
        print("2. Pop")
        print("3. Peek (view top)")
        print("4. Display stack")
        print("5. Check if empty")
        print("6. Show size")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            value = input("Enter the value to push: ")
            stack.push(value)
            print(f"'{value}' was pushed onto the stack.")
        elif choice == "2":
            if stack.is_empty():
                print("Stack underflow: the stack is empty, nothing to pop.")
            else:
                print(f"Popped: '{stack.pop()}'")
        elif choice == "3":
            if stack.is_empty():
                print("The stack is empty.")
            else:
                print(f"Top of the stack: '{stack.peek()}'")
        elif choice == "4":
            stack.display()
        elif choice == "5":
            print("The stack is empty." if stack.is_empty() else "The stack is not empty.")
        elif choice == "6":
            print(f"The stack has {stack.size()} item(s).")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 7.")


if __name__ == "__main__":
    main()
