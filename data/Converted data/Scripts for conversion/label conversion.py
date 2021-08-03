import collections

nodes = {}
with open("labels-usa-airports.txt") as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.replace("\n", "")
        node, label = line.split(" ")
        nodes[int(node)] = label        # og nodes with their labels
    ordered_nodes = collections.OrderedDict(sorted(nodes.items()))      # nodes sorted with their labels

    with open("ordered-labels-usa.txt", "w") as f_:
        for idx, (_, value) in enumerate(ordered_nodes.items()):
            f_.write(str(idx) + " " + value + "\n")
