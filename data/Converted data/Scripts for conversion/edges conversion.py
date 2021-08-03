nodes = {}
with open("ordered-labels-usa.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        new_node, old_node, _ = line.split(" ")
        nodes[old_node] = new_node
    # print(nodes)

    with open("usa-airports.edgelist") as f1:
        lines = f1.readlines()
        for line in lines:
            line = line.replace("\n", "")
            src, dst = line.split(" ")
            src = nodes[src]
            dst = nodes[dst]

            with open("bruh.txt", "a") as f2:
                f2.write(src + " " + dst + "\n")
