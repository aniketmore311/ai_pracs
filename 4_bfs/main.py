class Graph:
    def __init__(self):
        self.adjDict = dict()
        self.start_node = "S"
        self.goal_node = "G"
        self.path = list()

    def add_edge(self, u, v):
        if u not in self.adjDict:
            self.adjDict[u] = list()
        self.adjDict[u].append(v)

    def print(self):
        for key in self.adjDict:
            print(key)
            print(self.adjDict[key])

    def set_start_node(self, node):
        self.start_node = node

    def set_goal_node(self, node):
        self.goal_node = node

    def bfs(self):
        visited = list()
        q = list()
        visited.append(self.start_node)
        q.append(self.start_node)
        while q:
            node = q.pop(0)
            print(node, end=" ")
            if node == self.goal_node:
                print("\n", end="")
                return True
            children = list()
            if node in self.adjDict:
                children = self.adjDict[node]
            for child in children:
                if child not in visited:
                    visited.append(child)
                    q.append(child)
        print("\n", end="")
        return False


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
            graph.add_edge(parent, child)
    # graph.print()
    start_node = input("enter start node: ")
    goal_node = input("enter goal node: ")
    graph.set_start_node(start_node)
    graph.set_goal_node(goal_node)
    found = graph.bfs()
    if found:
        print(f"goal node {graph.goal_node} found")
    else:
        print(f"goal node {graph.goal_node} not found")


main()
