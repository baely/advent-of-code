import networkx as nx

with open("input.txt") as f:
    lines: list[str] = [line.strip() for line in f.read().strip().split("\n")]
    # nums: list[int] = list(map(int, lines))

G = nx.Graph()

for line in lines:
    parent, children_str = line.split(": ")
    children = children_str.split()

    for child in children:
        G.add_edge(parent, child)

cut_value, partition = nx.stoer_wagner(G)
print(len(partition[0]) * len(partition[1]))
