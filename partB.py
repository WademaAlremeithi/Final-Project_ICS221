#PART B
#Represent the road network using a graph
import networkx as nx
import matplotlib.pyplot as plt
class RoadNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_intersection(self, intersection_id):
        self.graph.add_node(intersection_id)

    def add_house(self, house_id, intersection_id):
        self.graph.add_node(house_id)
        #connect the house to the nearest intersection
        self.graph.add_edge(house_id, intersection_id)

    def add_road(self, intersection_from, intersection_to, road_id, road_name, length, weight):
        self.graph.add_edge(intersection_from, intersection_to, road_id=road_id, road_name=road_name, length=length, weight=weight)

    def draw(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=600, node_color='lightblue', font_weight='bold')
        edge_labels = {(u, v): f"{d['road_name']}\nWeight: {d['weight']}" for u, v, d in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()

#Point A to Point B in the shortest distance possible
#Using Dijkstra’s algorithm
def dijkstra(graph, start, end):
    #Create empty dictionaries for the distances and paths
    distances = {node: float('infinity') for node in graph}
    paths = {node: [] for node in graph}

    #Initialize the distance and path for start vertex
    distances[start] = 0
    paths[start] = [start]
    #create a set to keep track of visted vertices
    visited = set()

    #iterate until we reach end point(Point B)
    while end not in visited:
        shortest_dist = float('infinity')
        here = None
        for v in graph:
            if v not in visited and distances[v] < shortest_dist:
                shortest_dist = distances[v]
                here = v
        #Add the current vertex to visited 
        visited.add(here)
        #Update distances and paths for neighbors of the current vertex
        for neighbor in graph.neighbors(here):
            if neighbor not in visited:
                new_distance = distances[here] + graph[here][neighbor]['weight']
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    paths[neighbor] = paths[here] + [neighbor]
                
    return distances[end], paths[end]

def distribute_packages(self, start, end):
    #use the dijkstra's algorithm to find the shortest path considering both distance and traffic congestion
    return self.dijkstra(start, end)

#test cases
road_network = RoadNetwork()

#add intersections 
road_network.add_intersection("A")
road_network.add_intersection("B")
road_network.add_intersection("C")
road_network.add_intersection("D")

#add roads
road_network.add_road("A", "B", "1", "Sheikh Zayed Bin Sultan Street", 5, 0.5)
road_network.add_road("B", "C", "2", "Hamdan Bin Mohammed Street", 7, 0.3)
road_network.add_road("B", "D", "3", "Khalifa Bin Zayed Street, 6, 0.4)
road_network.add_road("C", "D", "4", "Al Salam Street", 5, 0.3)

#add houses
road_network.add_house("House1", "A")
road_network.add_house("House2", "B")
road_network.add_house("House3", "C")                      
road_network.add_house("House4", "D")

#draw the road network
road_network.draw()

#distribute packages
start_house = "House1"    
end_house = "House3"
shortest_distance, shortest_path = road_network.distribute_packages(start_house, end_house)
print(f"Shortest distance from {start_house} to {end_house}: {shortest_distance}")
print(f"Shortest path: {shortest_path}")
                      


    
                            
