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

    def dfid(self, depth_limit):
        for i in range(depth_limit+1):
            print(f"at level {i}")
            found = self.dls(i)
            if found:
                print(f"found {self.goal_node}")
                print(self.path)
                break
            else:
                print("not found")

    def dls(self, depth_limit):
        visited = list()
        path = list()
        found = self.dls_helper(visited, path, self.start_node, 0, depth_limit)
        if found:
            return True
        else:
            return False

    def dls_helper(self, visited, path, node, current_depth, depth_limit):
        if node in visited:
            return False
        if current_depth > depth_limit:
            return False
        visited.append(node)
        path.append(node)
        if node == self.goal_node:
            self.path = path.copy()
            return True

        children = []
        if node in self.adjDict:
            children = self.adjDict[node]
        for child in children:
            found = self.dls_helper(visited, path, child, current_depth+1, depth_limit)
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
    depth_limit = int(input("enter depth limit: "))
    graph.set_start_node(start_node)
    graph.set_goal_node(goal_node)
    graph.dfid(depth_limit)


main()
