**Precondition:**
```python
1 < len(matrix) <= 10
all(1 < len(row) <= 10 for row in matrix)
all(all(0 <= x < 10 for x in row) for row in matrix)
matrix[first[0]][first[1]] == matrix[second[0]][second[1]]
first != second
```