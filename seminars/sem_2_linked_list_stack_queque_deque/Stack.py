class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        # создаём новый узел и добавляем в него
        # новое значение data
        new_node = Node(data)
        # если ранее стек был пуст, значит первый элемент
        # и будет являться головой (head)
        if not self.top:
            self.top = new_node

        # если стек не пуст, то устанавливаем head
        # в качестве параметра next для нового узла
        new_node.next = self.top
        # записываем в head новый узел
        self.top = new_node
        self.size += 1

    def pop(self):
        if not self.top:
            return -1

        top = self.top

        if self.top.next != None:
            self.top = self.top.next

        else:
            self.top = None

        self.size -= 1
        return top.data



    def get_size(self):
        return self.size



def is_valid(bracket_sequence):
    stack = Stack()
    bracets_dict = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    for bracket in bracket_sequence:
        if bracket in bracets_dict:
            stack.push(bracket)
        elif stack.get_size() == 0 or bracket != bracets_dict[stack.pop()]:
            return False

    return stack.get_size() == 0

def is_palindrome(string):
    stack = Stack()
    for s in string:
        stack.push(s)

    for s in string:
        if s != stack.pop():
            return False

    return  True



# print(is_valid("()"))
# print(is_valid("({[]})"))
# print(is_valid("({[})"))
# print(is_valid("["))
# print(is_valid("()[]{}"))


# print(is_palindrome("racecar"))
# print(is_palindrome("level"))
# print(is_palindrome("python"))
# print(is_palindrome("madam"))

