
import heapq

"""
Wrapper Class Implementation for different Frontiers
"""

# Stack Data Structure(LIFO)
class Stack:
    # constructor
    def __init__(self):
        self.list = []

    # method to push the item to the stack
    def push(self, item):
        self.list.append(item)

    # method to pop the item from the stack
    def pop(self):
        return self.list.pop()

    # method to check if the stack is empty
    def isEmpty(self):
        return len(self.list) == 0


# Queue Data Structure(FIFO)
class Queue:
    # constructor
    def __init__(self):
        self.list = []

    # method to enqueue to the item to the queue
    def push(self, item):
        self.list.insert(0, item)

    # method to pop the next element in the queue
    def pop(self):
        return self.list.pop()

    # method to check if the queue is empty
    def isEmpty(self):
        return len(self.list) == 0



# Priority Queue Data Structure(FIFO)
class PriorityQueue:
    # constructor
    def __init__(self):
        self.heap = []
        self.count = 0

    # method to push item to PQ
    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)

    # method to pop the item with highest priority
    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item


    # method to check if the queue is empty
    def isEmpty(self):
        return len(self.heap) == 0

    # method to update the entry in the PQ
    def update(self,item, priority):
        #If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p,c,i) in enumerate(self.heap):
            if i == item:
                # if the current priority is already high no need to do anything
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break

        else:# else clause  for the 'for' loop(will execute this if above break statement is not executed)
            # just do normal push if the item is not in the heap
            self.push(item, priority) 


# priority queue with separate push function to detemine the priority of the element
class PriorityQueueWithFunction(PriorityQueue):
    def __init__(self, priorityFunction):
        self.priorityFunction = priorityFunction
        PriorityQueue.__init__(self)

    # use the priority function to calculate the priority number and use it to push the
    # item to  the heap
    def push(self, item):
        PriorityQueue.push(self, item, self.priorityFunction(item))


"""
HEURISTIC FUNCTIONS
"""
def nullHeuristic():
    return 0


# function to calculate manhattan distance
def manhattanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# function to calculate euclidian distance
def euclidianDistance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1])**2) ** 1/2






