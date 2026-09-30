import numpy as np


# 1. Create a 1D array of 10 integers and display array, size,
#    data type, and number of dimensions.

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:", arr)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Dimensions:", arr.ndim)


# 2. Create two arrays of 5 integers and perform arithmetic operations.

a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])
print("Array 1:", a)
print("Array 2:", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# 3. Find maximum, minimum, sum, and average.

arr = np.array([10, 25, 5, 40, 30, 15, 50, 35, 20, 45])
print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


# 4. Separate even and odd numbers using Boolean indexing.

arr = np.arange(1, 21)
print("Array:", arr)
print("Even numbers:", arr[arr % 2 == 0])
print("Odd numbers:", arr[arr % 2 != 0])


# 5. Reshape numbers 1 to 12 into 2x6, 3x4, and 4x3.

arr = np.arange(1, 13)
print("Original array:", arr)
print("2 x 6:\n", arr.reshape(2, 6))
print("3 x 4:\n", arr.reshape(3, 4))
print("4 x 3:\n", arr.reshape(4, 3))


# 6. Matrix addition of two 3x3 matrices.

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])
print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Matrix Addition:\n", a + b)


# 7. Matrix multiplication using an appropriate NumPy function.

a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[7, 8],
              [9, 10],
              [11, 12]])
print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Matrix Multiplication:\n", np.matmul(a, b))


# 8. Transpose of a 3x4 matrix.

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
print("Original matrix:\n", arr)
print("Transpose:\n", arr.T)


# 9. Access specific parts of a 4x4 array.

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
print("Matrix:\n", arr)
print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Diagonal elements:", np.diag(arr))
print("Second and third rows:\n", arr[1:3])


# 10. Sum of each row and each column separately.

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
print("Matrix:\n", arr)
print("Sum of each row:", np.sum(arr, axis=1))
print("Sum of each column:", np.sum(arr, axis=0))


# 11. Slicing: first 5, last 5, alternate, reverse.

arr = np.arange(1, 21)
print("Array:", arr)
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[-5:])
print("Alternate elements:", arr[::2])
print("Reverse order:", arr[::-1])


# 12. Replace elements greater than 50 with 0.

arr = np.array([10, 60, 25, 75, 40, 90, 55, 30, 80, 45])
print("Original array:", arr)
arr[arr > 50] = 0
print("After replacement:", arr)


# 13. Display unsorted array in ascending and descending order.

arr = np.array([50, 10, 40, 20, 80, 30, 70, 60])
print("Original array:", arr)
print("Ascending order:", np.sort(arr))
print("Descending order:", np.sort(arr)[::-1])


# 14. Find unique elements.

arr = np.array([1, 2, 2, 3, 4, 4, 5, 5, 6, 1])
print("Original array:", arr)
print("Unique elements:", np.unique(arr))


# 15. Concatenate two arrays horizontally and vertically.

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print("Array A:\n", a)
print("Array B:\n", b)
print("Horizontal concatenation:\n", np.hstack((a, b)))
print("Vertical concatenation:\n", np.vstack((a, b)))


# 16. Marks of 10 students: highest, lowest, average, median, std.

marks = np.array([78, 85, 67, 92, 74, 88, 95, 61, 80, 72])
print("Marks:", marks)
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))


# 17. Class average and marks above average.

marks = np.array([65, 72, 88, 91, 54, 76, 83, 69, 95, 81,
                  60, 74, 89, 93, 58, 77, 85, 67, 90, 71])
average = np.mean(marks)
print("Marks:", marks)
print("Class average:", average)
print("Marks above average:", marks[marks > average])


# 18. Create a 3D array of shape (2,3,4) containing 1 to 24.

arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:\n", arr)
print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# 19. Access elements from a 3D array.

arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:\n", arr)
print("First element:", arr[0, 0, 0])
print("Last element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])


# 20. Sum of all elements, each layer, rows, and columns.

arr = np.arange(1, 25).reshape(2, 3, 4)
print("3D Array:\n", arr)
print("Sum of all elements:", np.sum(arr))
print("Sum of each layer:", np.sum(arr, axis=(1, 2)))
print("Sum along rows (within each layer):\n", np.sum(arr, axis=2))
print("Sum along columns (within each layer):\n", np.sum(arr, axis=1))


# 21. Random 3D array; replace values greater than 50 with 0.

arr = np.random.randint(1, 101, size=(2, 3, 4))
print("Original random array:\n", arr)
arr[arr > 50] = 0
print("After replacing values > 50:\n", arr)


# 22. Random 3D array statistics.

arr = np.random.randint(1, 101, size=(3, 4, 5))
print("Random 3D array:\n", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# 23. Flatten a 3D array.

arr = np.arange(1, 25).reshape(2, 3, 4)
flat = arr.flatten()
print("Original 3D array:\n", arr)
print("Flattened array:", flat)


# 24. Flatten 1 to 27 and calculate statistics.

arr = np.arange(1, 28).reshape(3, 3, 3)
flat = arr.flatten()
print("Original 3D array:\n", arr)
print("Flattened array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))


# 25. Random 3D array, flatten it, and filter values.

arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
average = np.mean(flat)
print("Original 3D array:\n", arr)
print("Flattened array:", flat)
print("Elements greater than 50:", flat[flat > 50])
print("Even numbers:", flat[flat % 2 == 0])
print("Average:", average)
print("Elements less than average:", flat[flat < average])
