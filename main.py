# -*- coding: cp1251 -*-
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        if len(self.stack) <= 0:
            return None

    def size(self):
         return len(self.stack)

    def bracket(self, s: str):
        stack = []
        is_good = True
        for i in s:
            if i in '[{(':
                stack.append(i)
            elif i in ']})':
                if not stack:
                    is_good = False
                    break
                open_bracket = stack.pop()
                if open_bracket == '(' and i == ')':
                    continue
                if open_bracket == '{' and i == '}':
                    continue
                if open_bracket == '[' and i == ']':
                    continue
                is_good = False
                break
        if is_good and len(stack) == 0:
            print('Сбалансированно')
        else:
            print('Несбалансированно')


stack_ = Stack()
stack_.push('Hello')
print(stack_.pop())
print(stack_.peek())
print(stack_.size())
print(stack_.isEmpty())
stack_.bracket('({]{]{])')
stack_.bracket('({}{}{})')

