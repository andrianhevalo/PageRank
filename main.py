from helpers import generate_data
from pagerank import *


if __name__ == "__main__":
    # generate_data(20, 4)
    graph = create_graph()

    pagerank(graph)
    graph.print()
