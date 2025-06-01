class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
       
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def delete_nth_node(self, n):
        """Deletes the nth node in the list (1-based index)."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index should be a positive integer (1-based).")

        if n == 1:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range.")

        prev.next = current.next


if __name__ == "__main__":
    x = LinkedList()

    try:
        num_elements = int(input("Enter the number of elements in the linked list: "))
        for i in range(num_elements):
            val = int(input(f"Enter value for node {i + 1}: "))
            x.add_node(val)

        print("\nInitial Linked List:")
        x.print_list()

        delete_index = int(input("\nEnter the position (1-based index) of node to delete: "))
        x.delete_nth_node(delete_index)

        print("\nLinked List after deletion:")
        x.print_list()

    except ValueError:
        print("Invalid input. Please enter integers only.")

    print("\nAttempting to delete out-of-range node:")
    try:
        x.delete_nth_node(10)  
    except Exception as e:
        print("Error:", e)

    print("\nAttempting to delete from an empty list:")
    empty_x = LinkedList()
    try:
        empty_x.delete_nth_node(1)
    except Exception as e:
        print("Error:", e) 