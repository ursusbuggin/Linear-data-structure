"""
Assessment 3.2: Linear Data Structure
Program 1: Array (Python list) operations

A dynamic, menu-driven program. The user decides which operation to run
and what values to use. The array can grow and shrink while the program runs.
"""


def display(arr):
    """Traverse the array and print every element with its index."""
    if not arr:
        print("The array is empty.")
        return
    print("Array contents:")
    for index, value in enumerate(arr):
        print(f"  [{index}] -> {value}")
    print(f"Size: {len(arr)}")


def append_item(arr):
    """Insert a value at the end of the array."""
    value = input("Enter the value to add: ")
    arr.append(value)
    print(f"'{value}' was added at the end.")


def insert_at(arr):
    """Insert a value at a chosen position, shifting the others to the right."""
    value = input("Enter the value to insert: ")
    try:
        position = int(input(f"Enter the position (0 to {len(arr)}): "))
    except ValueError:
        print("Invalid position. Please enter a whole number.")
        return
    if position < 0 or position > len(arr):
        print("Position is out of range.")
        return
    arr.insert(position, value)
    print(f"'{value}' was inserted at position {position}.")


def delete_by_index(arr):
    """Remove the element at a chosen position."""
    if not arr:
        print("The array is empty. Nothing to delete.")
        return
    try:
        position = int(input(f"Enter the index to delete (0 to {len(arr) - 1}): "))
    except ValueError:
        print("Invalid index. Please enter a whole number.")
        return
    if position < 0 or position >= len(arr):
        print("Index is out of range.")
        return
    removed = arr.pop(position)
    print(f"'{removed}' was removed from position {position}.")


def delete_by_value(arr):
    """Remove the first element that matches the given value."""
    value = input("Enter the value to delete: ")
    if value in arr:
        arr.remove(value)
        print(f"'{value}' was removed.")
    else:
        print(f"'{value}' was not found in the array.")


def linear_search(arr):
    """Check each element from the start until the value is found."""
    target = input("Enter the value to search for: ")
    found_positions = []
    for index, value in enumerate(arr):
        if value == target:
            found_positions.append(index)
    if found_positions:
        print(f"'{target}' was found at index/indices: {found_positions}")
    else:
        print(f"'{target}' was not found.")


def update_item(arr):
    """Replace the value at a chosen position."""
    if not arr:
        print("The array is empty. Nothing to update.")
        return
    try:
        position = int(input(f"Enter the index to update (0 to {len(arr) - 1}): "))
    except ValueError:
        print("Invalid index. Please enter a whole number.")
        return
    if position < 0 or position >= len(arr):
        print("Index is out of range.")
        return
    new_value = input("Enter the new value: ")
    old_value = arr[position]
    arr[position] = new_value
    print(f"Index {position} changed from '{old_value}' to '{new_value}'.")


def remove_last(arr):
    """Remove the last element of the array (the 'REMOVE' step in the algorithm)."""
    if not arr:
        print("The array is empty. Nothing to remove.")
        return
    removed = arr.pop()
    print(f"'{removed}' was removed from the end.")


def main():
    arr = []
    while True:
        print("\n===== ARRAY OPERATIONS =====")
        print("1. Display array")
        print("2. Add item at the end")
        print("3. Remove last item")
        print("4. Insert item at a position")
        print("5. Delete item by index")
        print("6. Delete item by value")
        print("7. Search for an item")
        print("8. Update an item")
        print("9. Exit")
        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            display(arr)
        elif choice == "2":
            append_item(arr)
        elif choice == "3":
            remove_last(arr)
        elif choice == "4":
            insert_at(arr)
        elif choice == "5":
            delete_by_index(arr)
        elif choice == "6":
            delete_by_value(arr)
        elif choice == "7":
            linear_search(arr)
        elif choice == "8":
            update_item(arr)
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 9.")


if __name__ == "__main__":
    main()
