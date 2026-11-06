"""
Assessment 3.2: Linear Data Structure
Program 3: Queue (FIFO - First In, First Out)

A dynamic, menu-driven program. The user enqueues and dequeues values while
the program runs. The first item added is always the first one removed.

Note: this file is named queue_operations.py (not queue.py) on purpose, so it
does not clash with Python's built-in "queue" module.
"""


class Queue:
    def __init__(self):
        self.items = []  # index 0 is the "front", the end is the "rear"

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        """Add a value at the rear of the queue."""
        self.items.append(value)

    def dequeue(self):
        """Remove and return the front value. Returns None if empty."""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self):
        """Look at the front value without removing it."""
        if self.is_empty():
            return None
        return self.items[0]

    def rear(self):
        """Look at the rear value without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        """Show the queue from front to rear."""
        if self.is_empty():
            print("The queue is empty.")
            return
        print("Queue (front to rear):")
        print("  FRONT -> " + " | ".join(str(item) for item in self.items) + " <- REAR")


def main():
    queue = Queue()
    while True:
        print("\n===== QUEUE OPERATIONS (FIFO) =====")
        print("1. Enqueue (add to rear)")
        print("2. Dequeue (remove from front)")
        print("3. Peek front")
        print("4. Peek rear")
        print("5. Display queue")
        print("6. Check if empty")
        print("7. Show size")
        print("8. Exit")
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            value = input("Enter the value to enqueue: ")
            queue.enqueue(value)
            print(f"'{value}' joined the queue.")
        elif choice == "2":
            if queue.is_empty():
                print("Queue underflow: the queue is empty, nothing to dequeue.")
            else:
                print(f"Dequeued: '{queue.dequeue()}'")
        elif choice == "3":
            if queue.is_empty():
                print("The queue is empty.")
            else:
                print(f"Front of the queue: '{queue.front()}'")
        elif choice == "4":
            if queue.is_empty():
                print("The queue is empty.")
            else:
                print(f"Rear of the queue: '{queue.rear()}'")
        elif choice == "5":
            queue.display()
        elif choice == "6":
            print("The queue is empty." if queue.is_empty() else "The queue is not empty.")
        elif choice == "7":
            print(f"The queue has {queue.size()} item(s).")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 8.")


if __name__ == "__main__":
    main()
