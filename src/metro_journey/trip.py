import heapq
import json

#Part 1
def heuristic(node, goal):
    return 0

def a_star(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {vertex: float('inf') for vertex in graph}
    g_score[start] = 0

    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, color in graph[current].items():
            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score[neighbor] or (
                    tentative_g_score == g_score[neighbor] and color == graph[came_from[current]][current]):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return None


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def count_color_transitions(graph, path):
    transitions = 0
    for i in range(len(path) - 1):
        start_vertex = path[i]
        end_vertex = path[i+1]
        start_color = graph[start_vertex][end_vertex]
        if i < len(path) - 2:
            next_vertex = path[i+2]
            next_color = graph[end_vertex][next_vertex]
            if start_color != next_color:
                transitions += 1
    return transitions

with open('graph.json') as json_file:
    graph = json.load(json_file)

start_vertex = 'Первомайская'
goal_vertex = 'Тверская'

path = a_star(graph, start_vertex, goal_vertex)
time = (len(path) - 1)*3

if path:
    print(f"Минимальный путь от вершины {start_vertex} до вершины {goal_vertex}:")
    print(" -> ".join(path))
    num_trans = count_color_transitions(graph, path)
    print(num_trans)
    print(time+num_trans*3)
else:
    print(f"Путь от вершины {start_vertex} до вершины {goal_vertex} не найден.")

