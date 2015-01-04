rotate-array
============

What we want to do is rotate a N x N matrix
The way I kind of imagine this is basically transposing a row in the array into a column.

```
[[ 0, 1, 2, 3]

 [ 4, 5, 6, 7]

 [ 8, 9,10,11]

 [12,13,14,15]]
```
We want the first row to transpose into the last column:
0
1
2
3

Same for the second row etc..:

4,0

5,1

6,2

7,3

We can iterate through the matrix and do the transposition via the following:

`rotated[j][n-i-1] = array[i][j]`

The Row in the new matrix is the Col(j) of the old matrix
An example:
* Old Column 0 = New Row 0
* Old Column 1 = New Row 1 etc..


The Col of the new matrix is the dimension minus the Row(i) of the old matrix minus 1 (0 based array offset)
An example:

* For the old Row 1 the new coulmn = 4-0-1 = 3  
* For the old Row 2 the new coulmn = 4-1-1 = 2
* For the old Row 3 the new coulmn = 4-2-1 = 1
* For the old Row 4 the new coulmn = 4-3-1 = 0
