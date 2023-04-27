import heapq


class Graph:
    def __init__(self):
        super(Graph, self).__init__()
        self.vertices = dict()

    def addNode(self, node):
        self.vertices[node] = []

    def addEdge(self, node, edge):
        if self.hasVertex(node):
            self.vertices[node].append(edge)
        else:
            raise Exception("Node not found: ", node)

    def getVertices(self):
        return [v for v in self.vertices.keys()]

    def getEdges(self, node):
        if self.vertices.get(node):
            return self.vertices[node]
        else:
            raise Exception("Node not found: ", node)

    def hasVertex(self, node):
        return self.vertices.get(node) != None

    def printGraph(self):
        for k in self.vertices.keys():
            print(k)
            print(self.getEdges(k))
            print()


class UndirectedGraph(Graph):
    def __init__(self):
        super(UndirectedGraph, self).__init__()

    def addEdge(self, node, edge):
        v2 = edge[0]
        val = edge[1]
        if self.hasVertex(node) and self.hasVertex(v2):
            self.vertices[node].append(edge)
            self.vertices[v2].append((node, val))
        else:
            raise Exception("Node not found: ", node, v2)


class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0


class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0, item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)


class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """

    def __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction      # store the priority function
        PriorityQueue.__init__(self)        # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))


class TreeNode:
    def __init__(self, label, parent, cost=0, is_leaf=False):
        super(TreeNode, self).__init__()
        self.label = label
        self.parent = parent
        self.cost = cost
        self.children = []
        self.is_leaf = is_leaf
        if self.parent:
            self.parent.__addChild(self)

    def changeCost(self, newCost):
        self.cost = newCost

    def getCost(self):
        return self.cost

    def __addChild(self, node):
        self.children.append(node)

    def getChildren(self):
        return [n for n in self.children]

    def isLeaf(self):
        return self.is_leaf

    def print(self, indent):
        pad = ""
        for i in range(indent * 4):
            pad = pad + " "
        print(pad + self.label)
        for n in self.children:
            n.print(indent + 1)


pos_infinity = float('inf')
neg_infinity = float('-inf')
