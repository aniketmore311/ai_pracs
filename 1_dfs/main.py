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

    def dfs(self):
        visited = list()
        path = list()
        found = self.dfs_helper(visited, path, self.start_node)
        if found:
            print("found")
            print(self.path)
        else:
            print("not found")

    def dfs_helper(self, visited, path, node):
        if node in visited:
            return False
        if node == self.goal_node:
            path.append(node)
            self.path = path.copy()
            return True
        visited.append(node)
        path.append(node)
        children = []
        if node in self.adjDict:
            children = self.adjDict[node]
        for child in children:
            found = self.dfs_helper(visited, path, child)
            if found:
                return True
        path.pop()
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
    graph.dfs()

main()



