import itertools

def calculate_distance(route,matrix):
    total_distance =0
    for i in range(len(route)-1):
        total_distance+=matrix[route[i]][route[i+1]]
    total_distance+=matrix[route[-1]][route[0]]
    return total_distance

def shortest_distance(matrix):
    n =len(matrix)
    cities =list(range(n))
    shortest_route =None
    min_cost =float('inf')
    for i in itertools.permutations(cities[1:]):
        route =[0] +list(i)
        distance =calculate_distance(route,matrix)
        if distance<min_cost:
            min_cost =distance
            shortest_route=route
    return shortest_route,min_cost

matrix =[
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
best_route,min_cost =shortest_distance(matrix)
print(f"the best route is {best_route}\nthe minimum cost is {min_cost}")