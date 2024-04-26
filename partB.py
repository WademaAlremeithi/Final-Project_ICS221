#PART B
import networkx as nx
import matplotlib.pyplot as plt
class RoadNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_intersection(self, intersection_id):
        self.graph.add_node(intersection_id)

    def add_road(self, intersection_from, intersection_to, road_id, road_name, length, weight):
        self.graph.add_edge(intersection_from, intersection_to, road_id=road_id, road_name=road_name, length=length, weight=weight)

    def draw(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=600, node_color='lightblue', font_weight='bold')
        edge_labels = {(u, v): f"{d['road_name']}\nWeight: {d['weight']}" for u, v, d in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.show()