# v = ra's
# e = yal

class Graph:
    def __init__(self, dgraph=dict()):
        self.dgraph = dgraph

    def add_vertice(self):
        v = ''
        v = input('Enter node name: ')
        self.dgraph[v] = []

    def add_edge(self):
        e = []
        e = input('Enter two vertices (with space between): ').split()
        self.dgraph[e[0]].append(e[1])
        self.dgraph[e[1]].append(e[0])


    def shortest_path(self, initial, end):
        # initial = input('Enter initial: ')
        # end = input('Enter end: ')
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()
        
        while current_node != end:
            visited.add(current_node)
            destinations = self.dgraph[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = 1 + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)
            
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return 0
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        
        # Work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path

    def connectivity(self):
        for x in self.dgraph:
            agraph = self.dgraph.copy()
            agraph.pop(x)
            for y in agraph:
                s = self.shortest_path(x, y)
                if s == 0:
                    return 0
        return 1
                


dgraph = {'a':['a', 'b', 'c'], 'b':['a'], 'c':['a', 'd'], 'd':['c'], 'e':['f'], 'f':['e'] }
g = Graph(dgraph)