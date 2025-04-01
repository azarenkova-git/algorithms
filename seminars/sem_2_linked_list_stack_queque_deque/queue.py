import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
#Правильная ли реализация?
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.size += 1

    def appendleft(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.front.prev = new_node #можно ли менять эту и следующую строчку местами?
            new_node.next = self.front
            self.front = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None
        self.size -= 1
        return data

    def popleft(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        data = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        self.size -= 1
        return data

    def get_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        return self.rear.data

    def get_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        return self.front.data


def is_subsequence(a, b):
    q = Deque()
    for el in a:
        q.append(el)
    #print_deque(q)

    if len(a) == 0:
        return True
    else:
        for el in b:
            if el == q.get_front():
                q.popleft()
        return q.is_empty()

def print_deque(q):
    curr = q.front
    i = 0
    while i < q.get_size():
        print(curr.data)
        curr = curr.next
        i += 1


class TestIsSubsequence(unittest.TestCase):
    def test_valid_subsequences(self):

        self.assertTrue(is_subsequence("abc", "ahbgdc"))
        self.assertTrue(is_subsequence("ace", "abcde"))
        self.assertTrue(is_subsequence("", "abcde"))

    def test_invalid_subsequences(self):

        self.assertFalse(is_subsequence("axc", "ahbgdc"))
        self.assertFalse(is_subsequence("aec", "abcde"))
        self.assertFalse(is_subsequence("abcdef", "abc"))

    def test_edge_cases(self):

        self.assertTrue(is_subsequence("", ""))
        self.assertFalse(is_subsequence("a", ""))
        self.assertTrue(is_subsequence("a", "a"))
        self.assertFalse(is_subsequence("b", "a"))

if __name__ == "__main__":
    unittest.main()