def disconnected_users(net, users, source, crushes):
    def roads_to_station(grid):
        " Find what roads go to each station"
        roads = dict()
        for i, j in grid:
            if i not in roads:
                roads[i] = [j]
            else:
                roads[i].append(j)
            if j not in roads:
                roads[j] = [i]
            else:
                roads[j].append(i)
        return roads

    roads = roads_to_station(net)

    # delete crushing road
    for station in crushes:
        roads[station] = []

    working_stations = list(source)
    # go through the graph
    for station in working_stations:
        for next_station in roads[station]:
            if next_station not in crushes and next_station not in working_stations:
                working_stations.append(next_station)

    delivered_messages = 0
    if working_stations == crushes:
        return sum(users.values())

    for i in working_stations:
        delivered_messages += users[i]

    return sum(users.values()) - delivered_messages


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"
