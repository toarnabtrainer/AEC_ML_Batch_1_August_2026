# Pandas

<hr>

### Official site of Pandas
https://pandas.pydata.org/

<hr>

### Pandas Module in Python
Pandas is a popular Python library used for data manipulation and analysis. It provides two main data structures for working with data: Series (1-dimensional) and DataFrame (2-dimensional). The DataFrame is particularly useful for working with structured data, as it allows you to manipulate data using SQL-like operations.

Here are some of the main features of Pandas:

* **Reading and writing data:** Pandas can read and write data from and to a wide range of file formats, including CSV, Excel, SQL, and JSON.

* **Data manipulation:** Pandas provides a wide range of functions for manipulating data, including filtering, merging, reshaping, and grouping data.

* **Handling missing data:** Pandas provides functions for handling missing data, including filling in missing values and removing rows or columns with missing data.

* **Data visualization:** Pandas integrates with other popular data visualization libraries like Matplotlib and Seaborn to create visualizations of your data.

Here is an example of how to use Pandas to read in a CSV file and perform some basic operations on the data:

<pre>
import pandas as pd

# Read in the CSV file
df = pd.read_csv('my_data.csv')

# Print the first 5 rows of the DataFrame
print(df.head())

# Print some basic statistics about the data
print(df.describe())

# Filter the data to only include rows where the value in the 'column1' column is greater than 10
filtered_data = df[df['column1'] > 10]

# Group the data by the 'column2' column and calculate the mean of the 'column3' column for each group
grouped_data = df.groupby('column2')['column3'].mean()

# Plot a histogram of the 'column4' column
df['column4'].plot.hist()
</pre>

In the above example, we first import the Pandas library and read in a CSV file using the read_csv() function. We then perform some basic operations on the data, including printing the first 5 rows of the DataFrame, calculating some basic statistics about the data using the describe() function, filtering the data using boolean indexing, grouping the data using the groupby() function, and creating a histogram of one of the columns using the plot.hist() function.

<hr>

### Inbuilt Data Structures in Pandas in Python
Pandas is a Python library for data manipulation and analysis that provides several inbuilt data structures for handling data, including:

* **Series:** A one-dimensional array-like object that can hold any data type, including numerical, categorical, and textual data.

* **DataFrame:** A two-dimensional tabular data structure that consists of rows and columns, similar to a spreadsheet or SQL table.

* **Panel:** A three-dimensional data structure that can hold data with two or more dimensions. But it has become obsolete now and not in use.

Here are some of the main features of these data structures:

<u><b>Series:</b></u>
* **Indexing:** Series can be indexed using a label or position.
* **Arithmetic operations:** Series supports element-wise arithmetic operations.
* **Missing data handling:** Series can handle missing data using NaN (Not a Number).
* **Vectorized operations:** Series supports vectorized operations that can be applied to all elements of the Series at once.
* **Broadcasting:** Series supports broadcasting, which allows operations to be applied to subsets of the Series.

<u><b>DataFrame:</b></u>
* **Indexing:** DataFrame can be indexed using labels or positions for both rows and columns.
* **Selection:** DataFrame supports selection of specific rows or columns, as well as subsets of rows and columns.
* **Aggregation and grouping:** DataFrame can be aggregated and grouped based on the values in one or more columns.
* **Joining and merging:** DataFrame can be joined or merged with other DataFrame objects based on common columns.
* **Missing data handling:** DataFrame can handle missing data using NaN (Not a Number).
* **Data cleaning:** DataFrame provides functions for cleaning and transforming data, such as removing duplicates, filling missing values, and converting data types.

Overall, these inbuilt data structures in Pandas provide powerful tools for handling and analyzing data in Python.

<hr>

### Series Data Structure in Pandas
In pandas, a series is a one-dimensional array-like object that can hold any data type such as integers, strings, floating-point numbers, Python objects, etc. Series can be thought of as a column in a spreadsheet or a database table.

To create a Series in Pandas, you can use the pd.Series() constructor. For example, to create a Series of integers:

<pre>
import pandas as pd

my_series = pd.Series([1, 2, 3, 4, 5])
print(my_series)

Output:

0    1
1    2
2    3
3    4
4    5
dtype: int64

As you can see, the output shows the indices (0, 1, 2, 3, 4) and the corresponding values (1, 2, 3, 4, 5) of the Series.
</pre>

You can also specify the index labels explicitly:

<pre>
my_series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(my_series)

Output:

a    1
b    2
c    3
d    4
e    5
dtype: int64

In this case, the index labels are 'a', 'b', 'c', 'd', and 'e'.

You can access elements of a Series using the index:

print(my_series['c'])

Output:

3
</pre>

You can perform various operations on Series, such as arithmetic operations, aggregation functions, filtering, etc. For example, you can apply the sum() function to the Series to calculate the sum of its elements:

<pre>
print(my_series.sum())

Output:

15
</pre>

In addition to creating a Series from a list or array, you can also create a Series from a dictionary:

<pre>
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
my_series = pd.Series(my_dict)
print(my_series)

Output:

a    1
b    2
c    3
d    4
e    5
dtype: int64
</pre>

In this case, the dictionary keys are used as index labels, and the dictionary values are used as the corresponding Series values.

<hr>

### Data Frame Data Structure in Pandas
In Pandas, a DataFrame is a two-dimensional data structure, which can be thought of as a table. It is similar to a spreadsheet or SQL table, with rows and columns. Each column can have a different data type such as integer, float, string or even Python objects.

DataFrames can be created in several ways. They can be created by reading data from external files such as CSV or Excel files, or by converting other data structures such as lists or dictionaries to a DataFrame. Once created, data frames can be manipulated, queried, and analyzed using various functions and methods provided by Pandas.

Some of the key features of a Pandas DataFrame include:

* **Labelled Rows and Columns:** Each row and column in the DataFrame is labelled, which allows for easy and efficient indexing and selection of data.

* **Missing Data Handling:** Pandas DataFrame can handle missing data represented as NaN (Not a Number) values, and provides functions for imputing, dropping, or filling in missing values.

* **Indexing and Selection:** Pandas DataFrame allows for flexible indexing and selection of data based on rows, columns, and specific cell values.

* **Grouping and Aggregation:** Pandas DataFrame provides a powerful and flexible grouping and aggregation functionality that allows for performing statistical operations such as mean, sum, count, etc. on groups of data.

* **Joining and Merging:** Pandas DataFrame can be joined or merged with other data frames based on common columns or indices.

Overall, Pandas DataFrame is a versatile and powerful data structure that is widely used in data analysis, machine learning, and scientific computing.

<hr>

### Operations on Data Frame Data Structure in Pandas
Pandas provides a wide range of operations and functions to manipulate and analyze data frames. Some of the most commonly used operations on data frames are:

Indexing and selecting data: Data can be selected based on rows, columns, and cell values. This can be done using loc and iloc functions. loc function selects data based on labels, and iloc function selects data based on integer positions.

* **Filtering data:** Data frames can be filtered based on specific criteria using boolean indexing. This involves selecting rows based on a condition that evaluates to True or False.

* **Sorting data:** Data frames can be sorted based on one or more columns. Sorting can be done using the sort_values function.

* **Grouping and aggregating data**: Data frames can be grouped based on one or more columns, and various aggregation functions such as sum, mean, count, etc. can be applied to the groups.

* **Joining and merging data frames:** Data frames can be merged or joined based on common columns or indices. This can be done using the merge and join functions.

* **Data cleaning and transformation:** Data frames can be cleaned and transformed using various functions such as fillna, dropna, replace, and apply.

* **Statistical analysis:** Data frames can be analyzed using various statistical functions such as describe, corr, and covariance.

* **Data visualization:** Data frames can be visualized using various plotting functions such as scatter, histogram, and boxplot.

Overall, Pandas provides a wide range of operations and functions that can be used to manipulate, transform, and analyze data frames efficiently and effectively.

<hr>
