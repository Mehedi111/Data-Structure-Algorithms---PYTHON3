'''
TIME COMPLEXITY : O(n)
SPACE COMPLEXITY : O(n)
'''


class Stack:
    top = 0

    def __init__(self, stack_list, MAX):
        self.stack_list = stack_list
        self.MAX = MAX

    def push(self, item):
        if self.top < self.MAX:
            self.stack_list.append(item)
            self.top += 1
            print(f"{item} added to stack")
        else:
            print("Stack is full !")

    def pop(self):
        if self.top == 0:
            return "Stack is empty !"
        else:
            self.top -= 1
            return self.stack_list.pop(self.top)


if __name__ == '__main__':
    obj = Stack([], 30)

    #  PUSH 40 DATA TO STACK
    for i in range(1, 40):
        obj.push(i)

    #  POP ALL DATA FROM STACK
    for i in range(1, 40):
        print(obj.pop())
