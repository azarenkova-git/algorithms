class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def has_cycle(head):
    if head == None or head.next == None: #список пустой или состоит из одного элемента
        return False
    slow = head
    fast = head.next

    while slow != fast:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

def reverse_list(head):
    prev = None
    curr = head

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head

def middle_node(head):
    slow = fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow


def remove_elements(head, val):
    dummy = Node(0)
    dummy.next = head

    prev = dummy
    curr = head

    while curr != None:
        if curr.data == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next

def print_list(data):
    curr = data
    while curr != None:
        print(curr.data, ' ')
        curr = curr.next
    print()

def merge_arrays(l1, l2):
    dummy = Node(0)
    curr = dummy

    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2
    return dummy.next

if __name__ == "__main__":
    # Creating the list 3->5->8->10
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(8)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(7)
    #head.next.next.next.next = head.next.next


    #print_list(head)
    #print(has_cycle(head))
    #print(print_list(reverse_list(head)))
    #print(middle_node(head).data)
    #print(print_list(remove_elements(head, 9)))

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# 🔸 Создаём два списка: 1 -> 3 -> 5 и 2 -> 4 -> 6
l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

# 🚀 Тест
merged = merge_arrays(l1, l2)
print("Результат объединения:")
print_list(merged)

def list_to_linked(lst):
    if not lst:
        return None
    head = Node(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def linked_to_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

# 🔬 Тесты
def run_tests():
    tests = [
        # (list1, list2, expected_result)
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [4, 5, 6], [4, 5, 6]),
        ([], [], []),
        ([1, 2, 3], [10, 11], [1, 2, 3, 10, 11]),
        ([2, 4, 6], [2, 4, 6], [2, 2, 4, 4, 6, 6]),
        ([5], [3], [3, 5])
    ]

    for i, (a, b, expected) in enumerate(tests, 1):
        l1 = list_to_linked(a)
        l2 = list_to_linked(b)
        merged = merge_arrays(l1, l2)
        result = linked_to_list(merged)
        assert result == expected, f"❌ Test {i} failed: expected {expected}, got {result}"
        print(f"✅ Test {i} passed!")

run_tests()