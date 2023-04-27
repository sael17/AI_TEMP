from exam1 import UndirectedGraph, Queue, Stack, PriorityQueue
from exam1 import Graph,UndirectedGraph,Queue,Stack,PriorityQueue
from exam1 import TreeNode, pos_infinity, neg_infinity
from collections import defaultdict


def minmax(T: TreeNode):
  val = max_value(T)
  return val

def max_value(T):
  if not T.children:
    return T.cost
  vertice = neg_infinity
  for child in T.children:
    vertice = max(vertice, min_value(child))
  return vertice


def min_value(T):
  if not T.children:
    return T.cost
  vertice = pos_infinity
  for child in T.children:
    vertice = min(vertice, max_value(child))
  return vertice

def ufs(graph: UndirectedGraph, start, goal):
    frontier = PriorityQueue()
    frontier.push((start,[],0),0)
    explored = set()
    explored_costs = defaultdict(int)
    explored_costs[start] = 0
    while not frontier.isEmpty():
        current_state,current_path,current_cost = frontier.pop()
        if current_state == goal:
            return current_path + [current_state], current_cost
        for neighbor in graph.getEdges(current_state):
            new_cost = explored_costs[current_state] + neighbor[1]
            if neighbor[0] not in explored or new_cost < explored_costs[current_state]:
                explored_costs[neighbor[0]] = new_cost
                frontier.push((neighbor[0],current_path+[current_state],current_cost+neighbor[1]),new_cost)
    return None


def dfs(graph: UndirectedGraph, start, goal):
    frontier = Stack()
    explored = set()
    frontier.push((start, [], 0))
    while not frontier.isEmpty():
        current_state, current_path, current_cost = frontier.pop()
        if current_state == goal:
            return current_path + [current_state], len(current_path)
        if current_state not in explored:
            explored.add(current_state)
            for neighbor in graph.getEdges(current_state):
                if neighbor not in explored:
                    frontier.push(
                        (neighbor[0], current_path+[current_state], current_cost + neighbor[1]))
    return None


# DFS TEST CASES

#TEST CASE 1
G2 = UndirectedGraph()

G2.addNode('A')
G2.addNode('B')
G2.addNode('C')
G2.addNode('D')
G2.addNode('F')


G2.addEdge('A', ('B', 1))
G2.addEdge('A', ('C', 2))
G2.addEdge('B', ('C', 1))
G2.addEdge('B', ('D', 10))
G2.addEdge('D', ('C', 5))
G2.addEdge('B', ('F', 2))
G2.addEdge('C', ('F', 100))

print(dfs(G2, 'A', 'F'))


#TEST CASE 2
G2 = UndirectedGraph()

G2.addNode('A')
G2.addNode('B')
G2.addNode('C')
G2.addNode('D')
G2.addNode('F')


G2.addEdge('A', ('B', 1))
G2.addEdge('A', ('C', 2))
G2.addEdge('B', ('C', 1))
G2.addEdge('B', ('D', 10))
G2.addEdge('D', ('C', 5))
G2.addEdge('B', ('F', 2))
G2.addEdge('C', ('F', 100))

print(dfs(G2, 'A', 'C'))


#TEST CASE 3
G2 = UndirectedGraph()

G2.addNode('A')
G2.addNode('B')
G2.addNode('C')
G2.addNode('D')
G2.addNode('F')


G2.addEdge('A', ('B', 1))
G2.addEdge('A', ('C', 2))
G2.addEdge('B', ('C', 1))
G2.addEdge('B', ('D', 10))
G2.addEdge('D', ('C', 5))
G2.addEdge('B', ('F', 2))
G2.addEdge('C', ('F', 100))
G2.addNode('E')
G2.addEdge('E', ('F', 3))
print(dfs(G2, 'A', 'E'))


# MIN MAX TEST CASES

# Test case 1
N1 = TreeNode('1', None)
N2 = TreeNode('2', N1)
N3 = TreeNode('3', N1)
N4 = TreeNode('4', N2, 10, True)
N5 = TreeNode('5', N2, 8, True)
N6 = TreeNode('6', N3, 4, True)
N7 = TreeNode('7', N3, 5, True)

print(minmax(N1))


#Test case 2
N1 = TreeNode('1', None)
N2 = TreeNode('2', N1)
N3 = TreeNode('3', N1)
N4 = TreeNode('4', N2)
N5 = TreeNode('5', N2)
N6 = TreeNode('6', N3)
N7 = TreeNode('7', N3)
N8 = TreeNode('8', N4, 10, True)
N9 = TreeNode('9', N4, 9, True)
N10 = TreeNode('10', N5, 100, True)
N11 = TreeNode('11', N5, 8, True)
N12 = TreeNode('12', N6, 1, True)
N13 = TreeNode('13', N6, 2, True)
N14 = TreeNode('14', N7, 20, True)
N15 = TreeNode('15', N7, 4, True)

print(minmax(N1))


#Test case 3
N1 = TreeNode('1', None)
N2 = TreeNode('2', N1)
N3 = TreeNode('3', N1)
N4 = TreeNode('4', N2, 1, True)
N5 = TreeNode('5', N2, 2, True)
N6 = TreeNode('6', N3, 30, True)
N7 = TreeNode('7', N3, 20, True)

print(minmax(N1))


# UFS TEST CASES

#Test Case 1
G2 = UndirectedGraph()

G2.addNode('A')
G2.addNode('B')
G2.addNode('C')
G2.addNode('D')
G2.addNode('F')

G2.addEdge('A', ('B', 20))
G2.addEdge('A', ('C', 31))
G2.addEdge('B', ('C', 1))
G2.addEdge('B', ('D', 10))
G2.addEdge('D', ('C', 5))
G2.addEdge('B', ('F', 2))
G2.addEdge('C', ('F', 100))

print(ufs(G2, 'A', 'F'))


#Test Case 2
G2 = UndirectedGraph()

G2.addNode('A')
G2.addNode('B')
G2.addNode('C')
G2.addNode('D')
G2.addNode('F')

G2.addEdge('A', ('B', 20))
G2.addEdge('A', ('C', 31))
G2.addEdge('B', ('C', 1))
G2.addEdge('B', ('D', 10))
G2.addEdge('D', ('C', 5))
G2.addEdge('B', ('F', 2))
G2.addEdge('C', ('F', 100))

print(ufs(G2, 'A', 'C'))


#Test Case 3
G2 = UndirectedGraph()

G2.addNode('A')
G2.addNode('B')
G2.addNode('C')
G2.addNode('D')
G2.addNode('F')

G2.addEdge('A', ('B', 20))
G2.addEdge('A', ('C', 31))
G2.addEdge('B', ('C', 1))
G2.addEdge('B', ('D', 10))
G2.addEdge('D', ('C', 5))
G2.addEdge('B', ('F', 2))
G2.addEdge('C', ('F', 100))

G2.addNode('E')
G2.addEdge('E', ('F', 3))
print(ufs(G2, 'A', 'E'))
