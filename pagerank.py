class Node:
    def __init__(self, page, pr, links):
        self.page = page
        self.pr = pr
        self.links = links

    def print(self):
        st = ""
        print("Page: ", self.page)
        print("PageRank", self.pr)

        for link in self.links:
            st += str(str(link.page) + ", ")

        print("links: { " + st + " }")


class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, node_name):
        node = Node(node_name)
        self.nodes.append(node)

    def addEdge(self, p1, p2):
        n1, n2 = None, None
        for node in self.nodes:
            if node.page == p1:
                n1 = node
            elif node.page == p2:
                n2 = node
        if n1 and n2:
            n1.links[n1.links.index(n2.page)] = n2

    def getUniverse(self):
        return self.nodes

    def print(self):
        for node in self.nodes:
            node.print()


def create_graph():
    graph = Graph()

    with open("data_set.csv", "r") as file:
        for line in file.readlines()[1:]:
            temp_line = line.split(',')
            node = Node(int(temp_line[0]), int(temp_line[1]), [int(i) for i in temp_line[2].split()])
            graph.nodes.append(node)
        for node in graph.nodes:
            for link in node.links:
                graph.addEdge(node.page, link)
    return graph


def pagerank(graph):
    m = dict()
    nodes = graph.getUniverse()
    n = len(nodes)
    d = 0.85
    rp = float((1 - d) / n)
    me = 0.09
    for node in nodes:
        node.pr = float(1 / n)
    cf = True
    while cf:
        m.clear()
        s = 0
        for p in nodes:
            if p.links == []:
                s += float((d * p.pr) / n)

        for p in nodes:
            for link in p.links:
                m[link] = 0

        for p in nodes:
            for link in p.links:
                m[link] = float(p.pr / len(p.links))
        cf = False

        for p in nodes:
            if p not in m:
                p.pr = 0
            else:
                m[p] = rp + s + d * m.get(p)
                if abs(m[p] - p.pr) > me:
                    cf = True
                p.pr = m[p]
