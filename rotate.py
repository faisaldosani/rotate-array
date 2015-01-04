"""
Some examples of Algorithim design and development
of basic computer science examples.

I'm doing this for fun and just keeping my mind active :)
Its been many years since CSC101 and I feel like all the 
things you learn slowly escape you.
"""


#Array of N x N size
array = [[ 0, 1, 2, 3, 4],
         [ 5, 6, 7, 8, 9],
         [10,11,12,13,14],
         [15,16,17,18,19],
         [20,21,22,23,24]]
         
         
#function to rotate clockwise the matrix
def rotate(array):    
    #get the n dimensions         
    n = len(array)
    #make a empty array to rotate into
    rotated  = [[0 for x in range(n)] for x in range(n)]

    #O(n^2) implementation
    #We are looping through and basically transposing each row of the array
    #into a column
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = array[i][j]
    return rotated
        