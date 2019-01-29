class Vertex:
    # init creates a train station with name value and holds a dictionary with their edges (other stations)
    def __init__(self, value):
        self.value = value
        self.edges = {}

    # adds new station to edges dictionary with the corresponding weight (travel time for example)
    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    # returns all keys of the edges dictionary
    def get_edges(self):
        return list(self.edges.keys())
