def floyd_warshall(graph):
    n = len(graph)

    # Create the f array with the same values as the input .
    f = [[float('inf ')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j :
                f [i][j] = 0 # distance itself is 0
            elif graph[i][j] != 0:
                f [i][j] = graph[i][j]

    # Main loop for the algorithm
    for k in range(n):
        # Create a new array to hold the updated distances
        f_prime = [row[:] for row in f]

        for i in range(n):
            for j in range(n):
                f_prime[i][j] = min(f[i][j], f[i][k] + f[k][j])

        # Replace f by f_prime
        f = f_prime

    return f

graph = [
    [0 , 3 , 8 , 0 , -4] ,
    [0 , 0 , 0 , 1 , 7] ,
    [0 , 4 , 0 , 5 , 11] ,
    [2 , 5 , -5 , 0 , -2] ,
    [0 , 0 , 0 , 6 , 0]]

distances = floyd_warshall ( graph )
for row in distances:
    print(row)
