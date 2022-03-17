# We need to calculate the sums across the two diagonals of a square matrix. Along the first diagonal of the matrix, row index = column index. 
# The second diagonal is at (n - i - 1) column  for each row i . 
# Loop through the rows, summing both values as  increments

# Better Solution
# O(n) Time Complexity
# O(1) Space Complexity

# len(arr) gives the number of rows

def diagonalDifference(arr):
    # Write your code here, O(n)
    #l, r = left sum, right sum
    l, r = 0, 0
    # single pass, grab both values
    for i in range(len(arr)):
        l += arr[i][i]
        r += arr[i][-i-1] # same as arr[i][len(arr) - i - 1]
      # r += arr[i][(n-1)-i]
    return abs(l-r)