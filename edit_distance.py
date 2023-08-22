def edit_distance(str1, str2):

    #matrix = [[ i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    # init a matrix
    matrix = []
    for i in range(len(str1) + 1):
        row = []
        for j in range(len(str2) + 1):
            value = i + j
            row.append(value)
        matrix.append(row)


    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            # calculate k
            if(str1[i-1] == str2[j-1]):
                k = 0
            else:
                k = 1
            # insert, delete, replacement
            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+k)

    return matrix, matrix[len(str1)][len(str2)]

matrix, distance = edit_distance("escalator", "elevators")
print(matrix)
print(distance)
