'''
MOD RULES :

RULE 1: IF WE DIVIDED LARGE NUMBER WITH SMALL NUMBER THAN MOD WILL BE DIVISION OF LARGE NUMBER BY SMALL NUMBER
THAN MULTIPY THE DECIMAL VALUE WITH SMALL NUMBER THAN SUBTRACT LARGE NUMBER BY THE RESULT OF DIVISION
EXP: 10 % 3 = 1 => 10 // 3 = 3 => 3 * 3 = 9 => 10 - 9 = 1
EXP: 5 % 3 = 2 => 5 // 3 = 1 => 3 * 1 = 3 => 5 - 3 = 2
RULE 2: IF WE DIVIDED SMALL NUMBER WITH LARGE NUMBER THAN MOD WILL BE SMALL NUMBER
EXP: 100 % 102 = 100
RULE 3: IF WE DIVIDED SAME NUMBER WITH SAME NUMBER THAN MOD WILL BE 1
EXP : 100 % 100 = 1

    0 % 3 = 0
    1 % 3 = 1
    2 % 3 = 2
    3 % 3 = 0
    4 % 3 = 1
    5 % 3 = 2
    6 % 3 = 0
    7 % 3 = 1
    8 % 3 = 2
    9 % 3 = 0
    10 % 3 = 1

'''


class CircularQueue:
    head = 0
    tail = 0

    def __init__(self, queue_list, Q_SIZE):
        self.queue_list = queue_list
        self.Q_SIZE = Q_SIZE

    def enqueue(self, item):
        # Suppose head = 0, tail = 0+1 then 1 % 6 == 1 != head than tail = 0+1 % 6 = 1
        # Suppose head = 0, tail = 1+1 then 2 % 6 == 2 != head than tail = 1+1 % 6 = 2
        # Suppose head = 0, tail = 2+1 then 3 % 6 == 3 != head than tail = 2+1 % 6 = 3
        # Suppose head = 0, tail = 3+1 then 4 % 6 == 4 != head than tail = 0+1 % 6 = 4
        # Suppose head = 0, tail = 4+1 then 5 % 6 == 5 != head than tail = 0+1 % 6 = 5
        # Suppose head = 0, tail = 5+1 then 6 % 6 == 0 == head, so queue is Full Now
        if (self.tail + 1) % (self.Q_SIZE + 1) == self.head:
            print(f"Not Enqueue {item}, Queue is full !")
            return
        self.queue_list.insert(self.tail, item)
        self.tail = (self.tail + 1) % (self.Q_SIZE + 1)
        print(f"Enqueue {item} in queue !")

    def dequeue(self):
        if self.head == self.tail:
            return "Queue is Empty !"
        else:
            item = self.queue_list[self.head]
            self.head = (self.head + 1) % (self.Q_SIZE + 1)
            return (f"Dequeue {item} from queue")


if __name__ == '__main__':
    # initialization class  CircularQueue
    queue = CircularQueue([], 5)

    #  enqueue in queue
    for x in range(1, 8):
        queue.enqueue(x)

    #  dequeue in queue
    for x in range(3, 5):
        print(queue.dequeue())

    #  again enqueue
    for x in range(4, 6):
        queue.enqueue(x)

    #  again dequeue in queue
    for x in range(0, 5):
        print(queue.dequeue())


