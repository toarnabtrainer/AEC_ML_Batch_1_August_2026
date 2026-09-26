# ✅ Assignments on Pandas

### 🔰 Here are 5 practical assignments on Pandas covering dataFrame creation, duplicate detection, jion operations, group by and aggregations

## 🔵 Assignment 1 — Employee Data Exploration

Create a Pandas DataFrame containing at least **10 employees** with columns such as `Employee_ID`, `Name`, `Age`, `Gender`, `Department`, `Job` and `Salary`.

**Tasks:**

* Display the first 5 and last 3 records and examine the DataFrame using `info()` and `describe()`.
* Select specific columns and retrieve records using both `loc[]` and `iloc[]`.
* Filter employees based on conditions such as **Age > 30**, a particular gender, or selected jobs using `isin()`.
* Sort employees by `Salary` and `Age` in ascending/descending order.

**Expected Output:** A notebook showing the original dataset and results of each selection, filtering and sorting operation.

---

## 🔵 Assignment 2 — Sales Data Cleaning

Create or import a dataset containing `Order_ID`, `Product`, `Category`, `Quantity`, `Price` and `Salesperson`. Intentionally include some **missing and duplicate records**.

**Tasks:**

* Identify duplicate records using `duplicated()` and remove them using `drop_duplicates()`.
* Identify missing values using `isnull()` and calculate the number of missing values.
* Handle missing numerical values appropriately using `fillna()`.
* Create a calculated `Total_Amount` column using `Quantity × Price` and display the cleaned dataset.

**Expected Output:** Original vs cleaned dataset, including duplicate and missing-value analysis.

---

## 🔵 Assignment 3 — Customer Data Integration

Create three DataFrames: **Customers**, **Orders**, and **Customer_Location**, with an appropriate common identifier such as `Customer_ID`.

**Tasks:**

* Combine multiple customer datasets using `pd.concat()` and `ignore_index=True`.
* Merge Customers and Orders using `pd.merge()`.
* Demonstrate **Inner, Left, Right and Outer joins** and observe the differences.
* Produce a final consolidated DataFrame containing customer, order and location information.

**Expected Output:** Results of all four join types and the final consolidated customer dataset.

---

## 🔵 Assignment 4 — Sales Analysis using GroupBy and Pivot Tables

Using a sales dataset containing fields such as `Region`, `Salesperson`, `Product`, `Month`, `Quantity` and `Sales_Amount`, perform analytical operations.

**Tasks:**

* Use `groupby()` to calculate total and average sales by **Region**, **Product** and/or **Salesperson**.
* Identify the region/product with the highest sales.
* Create appropriate **Pivot Tables** to summarize sales across categories.
* Convert suitable wide-format data into long format using `pd.melt()` and export the final analysis to Excel.

**Expected Output:** Grouped summaries, Pivot Table, melted dataset and exported analysis.

---

## 🔵 Assignment 5 — Data Analysis and Visualization Mini-Project

Create or use a dataset containing at least **30 records** with multiple categorical and numerical attributes.

**Tasks:**

* Perform complete data exploration, filtering, sorting, duplicate checking and missing-value handling.
* Use `groupby()` and aggregation to derive meaningful business summaries.
* Create suitable visualizations to communicate important findings from the dataset.
* Present **at least 3 observations/insights** derived from the analysis.

**Expected Output:** A complete Jupyter Notebook containing **Data → Cleaning → Exploration → Analysis → Visualization → Insights**.

### Suggested progression

I would use **Assignments 1–2 after Pandas Session 1**, **Assignments 3–4 after Pandas Session 2**, and **Assignment 5 as the final Pandas hands-on exercise**.

This progression aligns well with the notebook coverage we used for the MCQs: **DataFrames → selection/filtering → sorting → duplicates/missing data → concatenation/merging → GroupBy → Pivot/Unpivot → visualization**.
