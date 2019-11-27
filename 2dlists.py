# 2D lists are more useful in datascience and AI
# 2D lists are nothing but the matrix which we used in maths
# a 3 * 3 matrix
# [
#   2 3 4
#   4 5 6
#   2 3 4
# ]
# 2D list a list where in each item in that list is another list

matrix = [
    [1,2,3],
    [2,3,4],
    [4,2,5]
]
print(matrix[0][1])
# assigning value to an 2d list variable
matrix[0][1] = 20
print(matrix[0][1])

# printing all elements in the matrix

for row in matrix:
    for item in row:
        print(item)