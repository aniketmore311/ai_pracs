import sys


class Graph:
    def __init__(self):
        self.adjDict = dict()
        self.start_node = "S"
        self.goal_node = "S"

    def add_edge(self, u, v, w):
        if u not in self.adjDict:
            self.adjDict[u] = list()
        self.adjDict[u].append([w ,v])

    def print(self):
        for key in self.adjDict:
            print(key)
            print(self.adjDict[key])

    def set_start_node(self, node):
        self.start_node = node

    def set_goal_node(self, node):
        self.goal_node = node

    def ucs(self):
        max_distance = sys.maxsize

        q = list()
        visited = list()
        q.append([0, self.start_node])
        # print(q)
        while q:
            # print(q)
            edge = q.pop(0)
            # print(q)
            if edge[1] in visited:
                continue
            visited.append(edge[1])
            if edge[1] == self.goal_node:
                if edge[0] < max_distance:
                    max_distance = edge[0]
            edges = []
            if edge[1] in self.adjDict:
                edges = self.adjDict[edge[1]]
            for outEdge in edges:
                # print(type(edge[0]))
                # print(type(outEdge[0]))
                q.append([edge[0] + outEdge[0], outEdge[1]])
                q.sort()
        print(f"min distance to goal node is: {max_distance}")


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
            graph.add_edge(parent, child.split(",")[0],int(child.split(",")[1]))
    # graph.print()
    start_node = input("enter start node: ")
    goal_node = input("enter goal node: ")
    graph.set_start_node(start_node)
    graph.set_goal_node(goal_node)
    graph.ucs()
    # graph.print()

main()
