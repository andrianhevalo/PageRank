import random
import csv


def generate_data(links_num, max_ptr):
    l = [i for i in range(links_num)]

    data_set = []

    for i in range(links_num):
        node_links = list(set([l[random.randint(0, len(l)-1)] for i in range(random.randint(1, max_ptr))]))

        if i in node_links:
            node_links.remove(i)

        node = {"page": i, "pr": 0, "links": ' '.join(str(link) for link in node_links)}

        data_set.append(node)

    with open('data_set.csv', 'w') as f:
        w = csv.writer(f)
        w.writerow(data_set[0].keys())

        for node in data_set:
            w.writerow(node.values())
