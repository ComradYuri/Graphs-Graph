class Graph:
    # Stores every vertex inside a dictionary
    # Vertex data (station names)is the key and the vertex instance is the value
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    # add vertex instances and names to graph dictionary
    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    # adds edges which are set in one direction
    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    # determines whether there is a patch between 2 vertices
    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print("Visiting " + current_vertex)
            # iterates through list of vertices. When a vertex is the end vertex is returns true
            if current_vertex == end_vertex:
                return True
            else:
                # prevents loops through graph
                # it only adds station to start if it hasn't already seen it
                vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]
        # if the while loop has finished and the end station has not been found it returns False
        return False
