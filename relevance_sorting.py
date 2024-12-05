def getSortedRelevanceIndices(R: list, old_indices: list = None) -> list:
    """Returns indices of sorted relevances (descending)"""

    indices = old_indices if old_indices else range(len(R))
    return sorted(indices, key=lambda i: R[i], reverse=True)


# Main program
number_of_parameters = int(input())
A = [int(i) for i in input().split()]  # list of parameters (a_i)
number_of_objects = int(input())


# Read features of objects from console
F = [[int(f) for f in input().split()] for _ in range(number_of_objects)]

# Calculate relevances for objects
R = [sum(A[j] * f[j] for j in range(len(A))) for f in F]
sorted_relevances_indices = getSortedRelevanceIndices(R)


number_of_requests = int(input())


for _ in range(number_of_requests):
    request = [int(i) for i in input().split()]

    if request[0] == 1:  # Query type 1: Output top-k most relevant objects
        print(*[i + 1 for i in sorted_relevances_indices[: request[1]]])

    elif request[0] == 2:  # Query type 2: Change value in matrix F and update relevance
        # Read and convert to 0-based index
        i, j, v = request[1] - 1, request[2] - 1, request[3]

        # Update relevance matrix
        R[i] = R[i] - F[i][j] + v
        F[i][j] = v

        sorted_relevances_indices = getSortedRelevanceIndices(R, sorted_relevances_indices)

    else:
        raise RuntimeError("Bad request!!!")
