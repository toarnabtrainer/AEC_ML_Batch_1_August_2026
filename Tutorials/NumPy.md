# NumPy

<hr>

### Official site of NumPy
https://numpy.org/

<hr>

### NumPy Module in Python
NumPy (Numerical Python) is a Python library used for working with arrays. It is one of the most popular libraries for numerical computing in Python. NumPy provides an efficient interface for working with large, multi-dimensional arrays and matrices, as well as a large collection of mathematical functions to operate on these arrays.

Here are some of the main features of NumPy:

* **Ndarray:** This is the main feature of NumPy, which provides a multidimensional array object that can hold elements of the same type. Ndarray objects can be created using various functions like array(), zeros(), ones(), empty(), etc.

* **Mathematical functions:** NumPy provides a wide range of mathematical functions like sin(), cos(), sqrt(), exp(), log(), etc., that can be applied to arrays and matrices.

* **Linear algebra functions:** NumPy provides a set of functions for performing various linear algebra operations like matrix multiplication, solving linear equations, finding eigenvalues and eigenvectors, etc.

* **Random number generation:** NumPy provides functions for generating random numbers, including both uniform and normal distributions.

* **Broadcasting:** NumPy allows operations to be performed on arrays of different shapes and sizes through a process called broadcasting.

Here is an example of how to use NumPy to create a simple array and perform some basic operations:

<pre>
import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])

# Print the array
print(arr)

# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Print the array
print(arr2d)

# Perform some basic operations on the array
print(arr + 5)
print(arr * 2)
print(arr2d + arr)
</pre>

In the above example, we first import the NumPy library and create a 1D array using the array() function. We then create a 2D array using the same function. Finally, we perform some basic operations on the arrays using arithmetic operators like + and *.

<hr>

### Numpy Ndarray in Python
NumPy ndarray is a multidimensional array object provided by the NumPy library in Python. It is the primary data structure used for scientific computing in Python due to its ability to perform efficient numerical operations on large arrays of data.

Here are some of the main features of NumPy ndarray:

* **Multidimensional arrays:** NumPy ndarray can be used to represent arrays of any dimensionality, including vectors, matrices, and higher-dimensional arrays.

* **Efficient numerical operations:** NumPy provides a wide range of numerical operations that can be applied to arrays of data, such as element-wise operations, matrix multiplication, and linear algebra operations.

* **Broadcasting:** NumPy allows arrays of different shapes to be used together in operations, using a technique called broadcasting.

* **Slicing and indexing:** NumPy provides powerful slicing and indexing operations for extracting subsets of arrays.

Here is an example of how to create and manipulate a NumPy ndarray:

<pre>
import numpy as np

# Create a 2D array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Print the array
print(a)

# Access an element of the array
print(a[0, 1])

# Slice the array
print(a[:, 1:])

# Perform element-wise operations
b = np.array([[2, 2, 2], [3, 3, 3]])
c = a + b
print(c)

# Perform matrix multiplication
d = np.array([[1], [2], [3]])
e = np.dot(a, d)
print(e)
</pre>

In the above example, we first import the NumPy library and create a 2D array using the array() function. We then access an element of the array using indexing, slice the array using slicing, perform element-wise operations using the + operator, and perform matrix multiplication using the dot() function.

<hr>

### Operations on Numpy Ndarray in Python
NumPy is a Python library used for working with arrays. It provides a variety of mathematical operations and functions to manipulate these arrays efficiently. Here are some of the most commonly used operations on NumPy ndarray in Python:

* **Creating an ndarray:** You can create an ndarray using the **numpy.array()** function. For example, **a = numpy.array([1, 2, 3])** creates a 1-dimensional array with elements 1, 2, and 3.

* **Accessing elements:** You can access elements in an ndarray using indexing. For example, **a[0]** would return the first element of the array **a**.

* **Slicing:** You can slice an ndarray to extract a portion of it using the : operator. For example, **a[1:3]** would return a new array with elements 2 and 3.

* **Reshaping:** You can change the shape of an ndarray using the numpy.reshape() function. For example, **a = numpy.array([1, 2, 3, 4, 5, 6])** followed by **a.reshape((2, 3))** creates a 2-dimensional array with 2 rows and 3 columns.

* **Concatenation:** You can concatenate two or more ndarrays together using the **numpy.concatenate()** function. For example, **numpy.concatenate((a, b))** would concatenate arrays **a** and **b**.

* **Transposing:** You can transpose an ndarray using the numpy.transpose() function. For example, **numpy.transpose(a)** would return the transpose of array **a**.

* **Arithmetic operations:** You can perform arithmetic operations on ndarrays. For example, **a + b** would add the corresponding elements of arrays **a** and **b**.

* **Mathematical functions:** NumPy provides a variety of mathematical functions to perform operations on ndarrays. For example, **numpy.sin(a)** would return a new array with the sine of each element in **a**.

* **Broadcasting:** NumPy provides a powerful feature called broadcasting, which allows arithmetic operations to be performed between ndarrays with different shapes. For example, **a + 1** would add 1 to each element in array **a**.

These are some of the most commonly used operations on NumPy ndarray in Python. There are many more advanced operations and functions available in NumPy, so it's worth exploring the documentation to learn more.

<hr>

### Broadcasting with Numpy Ndarray in Python
Broadcasting is a powerful feature in NumPy that allows arithmetic operations to be performed on arrays with different shapes. It eliminates the need to manually reshape arrays to match each other before performing the operation, which can be time-consuming and memory-intensive.

The basic rule of broadcasting is that two arrays are compatible for broadcasting if their dimensions match or if one of them has a dimension of 1. When the arrays are not compatible, NumPy will try to expand the smaller array to match the larger one by adding dimensions of size 1.

Here is an example of how broadcasting works:

<pre>
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])

c = a + b
print(c)
</pre>

In this example, **a** is a 1-dimensional array with shape (3,) and **b** is a 2-dimensional array with shape (3, 1). Since their shapes are not the same, NumPy will try to broadcast the arrays by adding a new dimension of size 1 to **a**, resulting in a shape of (3, 1). Now the arrays are compatible, and NumPy will perform the element-wise addition between **a** and **b**.

The output of the code above will be:

<pre>
array([[2, 3, 4],
       [3, 4, 5],
       [4, 5, 6]])
</pre>

As you can see, broadcasting has allowed us to perform the addition between **a** and **b** without explicitly reshaping the arrays to match each other. This is a powerful feature that can simplify code and improve performance.

It's important to note that broadcasting can lead to unexpected results if the dimensions of the arrays are not properly understood. It's always a good practice to check the shapes of the arrays before performing arithmetic operations.

<hr>
