with open("ordered-usa.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        node, label = line.split(" ")
        with open("ordered-usa.csv", 'a') as f1:
            f1.write(node + ',' + label + '\n')