# ✅ Assignments on NumPy

### 🔰 Here are 5 practical assignments, progressing from array fundamentals to array manipulation, filtering, missing values, and broadcasting.

## 🔵 Assignment 1 — NumPy Array Creation and Exploration

Create different **1D and 2D NumPy arrays** containing numerical data.

**Tasks:**

* Create arrays using `np.array()`, `np.zeros()` and `np.linspace()`.
* Examine arrays using `shape`, `ndim`, `size` and `dtype`.
* Create a 2D array and access individual rows, columns and elements using indexing/slicing.
* Convert an appropriate array into a different shape using `reshape()`.

**Expected Output:** Display each array along with its dimensions, shape, data type and reshaped form.

---

## 🔵 Assignment 2 — Reshaping and Array Manipulation

Create a NumPy array containing at least **20 numerical values**.

**Tasks:**

* Reshape the array into different dimensions using `reshape()`, including the use of `-1`.
* Transpose a 2D array and compare its original and transposed shapes.
* Convert a multidimensional array into a 1D array using `flatten()`.
* Reverse and sort the array, including sorting numerical values in descending order.

**Expected Output:** Original, reshaped, transposed, flattened, reversed and sorted arrays.

---

## 🔵 Assignment 3 — Array Modification and Combination

Create multiple NumPy arrays representing numerical datasets.

**Tasks:**

* Add new values to an array using `np.append()`.
* Perform suitable insert/delete operations demonstrated during the session.
* Combine compatible arrays using `np.concatenate()`.
* Combine arrays using `np.stack()` and observe how the resulting dimensions differ from concatenation.

**Expected Output:** Display the arrays before and after each manipulation and explain the difference between **concatenation and stacking**.

---

## 🔵 Assignment 4 — Indexing, Filtering, Views and Copies

Create a **two-dimensional NumPy array** containing a suitable range of numerical values.

**Tasks:**

* Retrieve selected rows and columns using NumPy indexing and slicing.
* Use Boolean indexing to extract values satisfying conditions such as `> 20`, `< 50`, etc.
* Create a **view** of the array, modify it and observe the effect on the original array.
* Create a **copy**, modify it and compare its behavior with the view.

**Expected Output:** Selected/filtered values and a clear demonstration of the difference between a NumPy **view and copy**.

---

## 🔵 Assignment 5 — Numerical Data Processing with NumPy

Create a NumPy array representing a numerical dataset such as **employee salaries, product sales, student marks or monthly production figures**. Include some `NaN` values where appropriate.

**Tasks:**

* Identify missing (`NaN`) values using `np.isnan()` and identify unique values using `np.unique()`.
* Perform suitable numerical/statistical operations on the dataset.
* Filter records using Boolean conditions and derive meaningful subsets.
* Demonstrate a suitable **broadcasting operation** on the dataset and explain the resulting output.

**Expected Output:** A Jupyter Notebook showing **Data Creation → Inspection → Missing/Unique Value Analysis → Filtering → Numerical Processing → Broadcasting → Final Results**.

### Recommended progression

I would use **Assignments 1–2 as foundational exercises**, **Assignments 3–4 for intermediate hands-on practice**, and **Assignment 5 as the final NumPy mini-assignment**.

Together they reinforce the major areas covered in your notebook: **array creation → shape/dimensions → reshape/transpose/flatten → append and combination → indexing/slicing → views/copies → Boolean filtering → NaN/unique values → numerical operations → broadcasting**.
