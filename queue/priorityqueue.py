class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self,data):
        self.queue.append(data)
    
    def delete(self):
        try:
            maxElemIndex = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[maxElemIndex]:
                    maxElemIndex = i
            item = self.queue[maxElemIndex]
            del self.queue[maxElemIndex]
            return item
        except IndexError:
            print()
            exit()

if __name__ == '__main__':
    numQueue = PriorityQueue()
    numQueue.insert(15)
    numQueue.insert(10)
    numQueue.insert(1999)
    print('\nAfter Insertion of elements in Queue:')
    print(numQueue)
    print('\nQueue removing elements based on Priority (Largest num to be removed)')
    while not numQueue.isEmpty():
        print(numQueue.delete())
