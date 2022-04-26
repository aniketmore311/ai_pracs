import sys


class Graph:
    def __init__(self):
        self.adjDict = dict()
        self.start_node = "S"
        self.goal_node = "S"
        self.heuristics = dict()

    def add_edge(self, u, v, w):
        if u not in self.adjDict:
            self.adjDict[u] = list()
        self.adjDict[u].append([v, w])

    def add_heuristic(self, node, val):
        self.heuristics[node] = val

    def print(self):
        for key in self.adjDict:
            print(key)
            print(self.adjDict[key])

    def set_start_node(self, node):
        self.start_node = node

    def set_goal_node(self, node):
        self.goal_node = node

    def astar(self):
        max_distance = sys.maxsize
        q = list()
        fx = self.heuristics[self.start_node] + 0
        q.append([fx, self.start_node])
        while q:
            pair = q.pop(0)
            fx = pair[0]
            node = pair[1]
            dist_so_far = fx - self.heuristics[node]
            if node == self.goal_node:
                if dist_so_far < max_distance:
                    max_distance = dist_so_far
            children = []
            if node in self.adjDict:
                children = self.adjDict[node]
            for edge in children:
                child = edge[1]
                weight = edge[0]
                q.append([dist_so_far + weight + self.heuristics[child], child])
                q.sort()
        print(f"min distance to goal node is {max_distance}")


def main():
    print("enter input")
    graph = Graph()
    while True:
        tokens = input().split()
        parent = tokens[0]
        if parent == "-1":
            break
        children = tokens[1:]
        for child in children:
            # print(child)
            # print(child.split(","))
            graph.add_edge(parent, int(child.split(",")[1]), child.split(",")[0])
    while True:
        tokens = input().split()
        node = tokens[0]
        if node == "-1":
            break
        value = int(tokens[1])
        graph.add_heuristic(node, value)
    # print(graph.adjDict)
    # print(graph.heuristics)
    # graph.print()
    start_node = input("enter start node: ")
    goal_node = input("enter goal node: ")
    graph.set_start_node(start_node)
    graph.set_goal_node(goal_node)
    graph.astar()

main()
