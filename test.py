#-------------Smart Emergency Evacuation System using A* Algorithm----------------#

import networkx as nx
import heapq

# Subjects
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']

# Students enrolled (overlap creates conflict)
enrollment = {
    'Math': ['A', 'B', 'C'],
    'Physics': ['B', 'C', 'D'],
    'Chemistry': ['C', 'E'],
    'Biology': ['D', 'E'],
    'English': ['A', 'E']
}

# Create graph
G = nx.Graph()

# Add nodes
for sub in subjects:
    G.add_node(sub)

# Add edges (conflicts)
for i in subjects:
    for j in subjects:
        if i != j:
            # Check if there is any common student
            if set(enrollment[i]) & set(enrollment[j]):
                G.add_edge(i, j)

# Graph coloring (assign time slots)
coloring = nx.coloring.greedy_color(G, strategy='largest_first')

# Convert colors to time slots
time_slots = {
    0: "Slot 1",
    1: "Slot 2",
    2: "Slot 3",
    3: "Slot 4"
}

print("Exam Timetable:\n")

for subject, color in coloring.items():
    print(subject, "→", time_slots[color])


def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    parent = {}
    while pq:
        _, current = heapq.heappop(pq)
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]
        for neighbor, dist, risk in graph[current]:
            cost = dist + risk # combine distance + risk
            new_g = g_cost[current] + cost
            if new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (f, neighbor))
                parent[neighbor] = current
    return None

# Run
path = a_star('A', 'F')
print("Safest Path:", path)







#-------------Intelligent Traffic Signal Control using A* Algorithm----------------#
import heapq


start = (10, 8, 6, 4)


# Define "good enough" goal
def is_goal(state):
    return sum(state) <= 5   # near-zero traffic


def heuristic(state):
    return sum(state)


def get_neighbors(state):
    N, S, E, W = state
    neighbors = []
    
    # NS Green
    ns = (
        max(0, N - 4),
        max(0, S - 4),
        E + 1,
        W + 1
    )

    # EW Green
    ew = (
       N + 1,
        S + 1,
        max(0, E - 4),
        max(0, W - 4)
    )


    neighbors.append(("NS", ns))
    neighbors.append(("EW", ew))


    return neighbors


def a_star(start):
    pq = []
    heapq.heappush(pq, (0, start))


    g_cost = {start: 0}
    parent = {}
    action_taken = {}
    visited = set()


    while pq:
        _, current = heapq.heappop(pq)


        if is_goal(current):
            path = []
            actions = []


            while current in parent:
                path.append(current)
                actions.append(action_taken[current])
                current = parent[current]


            path.append(start)
            return path[::-1], actions[::-1]


        if current in visited:
            continue
        visited.add(current)


        for action, neighbor in get_neighbors(current):


            new_g = g_cost[current] + sum(neighbor)


            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + heuristic(neighbor)


                heapq.heappush(pq, (f, neighbor))
                parent[neighbor] = current
                action_taken[neighbor] = action


    return None, None


# Run
path, actions = a_star(start)


print("Traffic Optimization:\n")


for i in range(len(path)):
    print(f"State {i}: {path[i]}")
    if i < len(actions):
        print(f"  → Action: {actions[i]}")



#-------------Web Crawler Implementation using BFS and DFS Algorithms------------------#
from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs_crawler(start):
    visited = set()
    queue = deque([start])


    print("BFS Traversal:")


    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)


            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


bfs_crawler('A')







#DFS Crawler
# graph definition copied from the BFS crawler cell for self-containment
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs_crawler(start):
    visited = set()
    stack = [start]


    print("\nDFS Traversal:")


    while stack:
        node = stack.pop()


        if node not in visited:
            print(node, end=" ")
            visited.add(node)




            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


dfs_crawler('A')



#-------------Optimal Classroom Seating Arrangement using Hill Climbing Algorithm-----------------#
import random


# Generate students
students = []
for i in range(30):
    students.append({
        "id": i,
        "academic": random.randint(1, 10),
        "discipline": random.randint(1, 10)
    })

# Example conflict pairs
conflicts = {(1, 2), (5, 6), (10, 11)}

# Create initial seating (5x6)
def create_seating():
    s = students[:]
    random.shuffle(s)
    return [s[i*6:(i+1)*6] for i in range(5)]

# Fitness function
def fitness(seating):
    score = 0
    for i in range(5):
        for j in range(6):
            student = seating[i][j]
            # Check neighbors (right & down only to avoid double counting)
            if j < 5:
                neighbor = seating[i][j+1]
                score += 10 - abs(student["academic"] - neighbor["academic"])
                if (student["id"], neighbor["id"]) in conflicts:
                    score -= 20
            if i < 4:
                neighbor = seating[i+1][j]
                score += 10 - abs(student["academic"] - neighbor["academic"])
                if (student["id"], neighbor["id"]) in conflicts:
                    score -= 20
    return score


# Generate neighbor (swap two students)
def get_neighbor(seating):
    new = [row[:] for row in seating]


    r1, c1 = random.randint(0,4), random.randint(0,5)
    r2, c2 = random.randint(0,4), random.randint(0,5)


    new[r1][c1], new[r2][c2] = new[r2][c2], new[r1][c1]
    return new


# Hill Climbing
def hill_climbing():
    current = create_seating()
    current_score = fitness(current)


    for _ in range(1000):
        neighbor = get_neighbor(current)
        neighbor_score = fitness(neighbor)
        if neighbor_score > current_score:
            current = neighbor
            current_score = neighbor_score


    return current, current_score


# Run
best_seating, best_score = hill_climbing()


print("Best Fitness Score:", best_score)




#-------------Exam Timetable Optimization using Graph Coloring Technique-----------------#
import networkx as nx

# Subjects
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']


# Students enrolled (overlap creates conflict)
enrollment = {
    'Math': ['A', 'B', 'C'],
    'Physics': ['B', 'C', 'D'],
    'Chemistry': ['C', 'E'],
    'Biology': ['D', 'E'],
    'English': ['A', 'E']
}


# Create graph
G = nx.Graph()


for sub in subjects:
    G.add_node(sub)


# Add edges (conflicts)
for i in subjects:
    for j in subjects:


        if i != j:
            if set(enrollment[i]) & set(enrollment[j]):
                G.add_edge(i, j)


# Graph coloring (assign time slots)
coloring = nx.coloring.greedy_color(G, strategy='largest_first')


# Convert colors to time slots
time_slots = {0: "Slot 1", 1: "Slot 2", 2: "Slot 3", 3: "Slot 4"}


print("Exam Timetable:\n")
for subject, color in coloring.items():
    print(subject, "→", time_slots[color])
