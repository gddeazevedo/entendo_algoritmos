import math


# Graph table
graph: dict[str, dict[str, int]] = {}

graph["start"] = {"a": 6, "b": 2}
graph["a"] = {"end": 1}
graph["b"] = {"a": 3, "end": 5}
graph["end"] = {} # end node does not have neighbours

# Costs table
costs: dict[str, int | float] = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = math.inf

# Parents table
parents: dict[str, str | None] = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

# Array to keep track of the processed nodes
processed = []


def find_lowest_cost_node(costs: dict[str, int | float]):
    global processed

    lowest_cost = math.inf
    lowest_cost_node = None

    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def dijkstras_algorithm():
    global costs
    global graph
    global parents
    global processed

    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbours = graph[node]

        for neighbour_node, neighbour_cost in neighbours.items():
            new_cost = cost + neighbour_cost

            if new_cost < costs[neighbour_node]:
                costs[neighbour_node] = new_cost
                parents[neighbour_node] = node

        processed.append(node)
        node = find_lowest_cost_node(costs)
 
    print(parents) # shortest path
