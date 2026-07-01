maze = {
    "S": "1",
    "1": ["2", "3"],
    "2": ["4", "5"],
    "3": [],
    "4": [],
    "5": ["6", "F"],
    "6": ["7", "8"],
    "F": [],
    "7": ["9", "10"],
    "8": [],
    "9": ["11", "12"],
    "10": [],
    "11": [],
    "12": ["13", "14"],
    "13": [],
    "14": ["15", "16"],
    "15": [],
    "16": [],
}

root = "S"
target = "F"

queue = [root]
parents = {}
while queue:
    current_vertex = queue.pop(0)
    if current_vertex == target:
        queue = []
    else:
        for neighbor in maze[current_vertex]:
            parents[neighbor] = current_vertex
            queue.append(neighbor)


def print_path(root, target, parents):
    """Print path to target from root using parents."""

    vertex = target
    path = [vertex]
    while vertex is not root:
        path.append(parents[vertex])
        vertex = parents[vertex]

    path.reverse()

    return path


print_path(root, target, parents)
