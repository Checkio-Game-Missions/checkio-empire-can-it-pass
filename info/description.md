You are given a matrix (2D array) and the coordinates (row and column) of two cells with the same value.
The matrix consists of digits. You may move to neighbouring cells either horizontally or
vertically provided the values of the origin and destination cells are equal.
You should determine if a path exists between two given cells.

A matrix is represented as a tuple of tuples with digits.
Coordinates are represented as a tuple with two numbers: row and column.
The result should be any value which can be converted into a boolean. If a path exists, then return True.
Return False if there is none.

```
From [1, 1] to [5, 5] == true
 0 * 0   5   4   0
 *             
 0   1   5   0   0
 *             
 0 * 0 * 0   7   2
     *   *     
 8   0 * 0 * 0 * 0
         *       *               
 0   9   0   1   0
 
From [1, 1] to [1, 5] == true
 0 * 0   5   4   0
 *                             
 0   1   5   0   0
 *             
 0 * 0 * 0   7   2
     *   *     
 8   0 * 0   4   0
         *                       
 0   9   0   1   0
```
