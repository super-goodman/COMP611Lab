class Graph :
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self , v , u , w ):
        self.edges.append((v , u , w))

    def bellman_ford (self , src):
        # Initialize distances
        d = [float ("Inf")] * (self.V + 1) # starting from 1
        d[src] = 0

        # Repeat |V| - 1 times
        for _ in range(self.V + 1):
            d_prime = list(d) # Copy current distances to d’

        for v , u , w in self.edges :
            d_prime[u] = min (d_prime[u], d[v] + w)

            d = d_prime # Replace d by d’

        # Print distances
        self.print_distances(d)

    def print_distances (self , dist):
        print("Vertex Distance from Source")
        for i in range (1 , len(dist)): # Start from 1
            print("{0}\ t\t{1}".format (i, dist[i]))

# Example On Slide 21

graph = Graph (5)
graph.add_edge (1 , 2 , 6)
graph.add_edge (1 , 4 , 7)
graph.add_edge (2 , 3 , 5)
graph.add_edge (2 , 4 , 8)
graph.add_edge (2 , 5 , -4)
graph.add_edge (3 , 2 , -2)
graph.add_edge (4 , 3 , -3)
graph.add_edge (4 , 5 , 9)
graph.bellman_ford(1)
