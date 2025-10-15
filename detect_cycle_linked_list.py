class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next  # ❌ Should move two steps
        if slow == fast:
            return True
    return False


# Example
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a  # Cycle
print(has_cycle(a))  # Expected True
