
---

# ✅ Complete Note on Pivot and Unpivot Operations

## ☑️ 1) What are Pivot and Unpivot?

In data handling, tables are often stored in two common shapes:

### 🔴 Wide format

A table where one entity is represented in a **single row**, and multiple related values are stored in **different columns**.

### 🔴 Long format

A table where related values are stored in **multiple rows** instead of many columns. Usually there is:

* an **identifier column**
* a **category/attribute column**
* a **value column**

---

## ☑️ 2) Main Idea

### 🔴 Unpivot

**Unpivot** converts a **wide table into a long table**.

It takes multiple columns and turns them into rows.

### 🔴 Pivot

**Pivot** converts a **long table into a wide table**.

It takes row values and spreads them across columns.

---

# ✅ 3) Why do we need them?

These operations are very common in:

* Excel
* Power BI
* SQL
* Pandas
* data cleaning
* reporting
* dashboard preparation
* machine learning preprocessing

### 🔴 Use Unpivot when:

* your data has repeated measurements across columns
* you want a normalized structure
* you need to make charts or dashboards
* you want easier filtering/grouping

### 🔴 Use Pivot when:

* you want summary reports
* you want categories shown as separate columns
* you want a compact presentation
* you need cross-tabulation

---

# ✅ 4) Understanding Wide vs Long Format

## ☑️ Wide Format Example

| StudentID | Name | Math | Science | English |
| --------- | ---- | ---- | ------- | ------- |
| 101       | Asha | 85   | 90      | 88      |
| 102       | Ravi | 78   | 82      | 80      |
| 103       | Neha | 92   | 89      | 95      |

In this table:

* each student is one row
* subject names are column headers
* marks are spread across columns

This is **wide format**.

---

## ☑️ Long Format Example

| StudentID | Name | Subject | Marks |
| --------- | ---- | ------- | ----- |
| 101       | Asha | Math    | 85    |
| 101       | Asha | Science | 90    |
| 101       | Asha | English | 88    |
| 102       | Ravi | Math    | 78    |
| 102       | Ravi | Science | 82    |
| 102       | Ravi | English | 80    |
| 103       | Neha | Math    | 92    |
| 103       | Neha | Science | 89    |
| 103       | Neha | English | 95    |

Now:

* one student appears in multiple rows
* subject moved into a column
* marks are stored in one value column

This is **long format**.

---

# ✅ 5) Unpivot: Wide to Long

## ☑️ Definition

Unpivot transforms selected columns into two columns:

* one for the **former column names**
* one for the **corresponding values**

---

## ☑️ Example 1: Student Marks

### 🔴 Original Wide Table

| StudentID | Name | Math | Science | English |
| --------- | ---- | ---- | ------- | ------- |
| 101       | Asha | 85   | 90      | 88      |
| 102       | Ravi | 78   | 82      | 80      |

### 🔴 After Unpivot

| StudentID | Name | Subject | Marks |
| --------- | ---- | ------- | ----- |
| 101       | Asha | Math    | 85    |
| 101       | Asha | Science | 90    |
| 101       | Asha | English | 88    |
| 102       | Ravi | Math    | 78    |
| 102       | Ravi | Science | 82    |
| 102       | Ravi | English | 80    |

### 🔴 What happened?

The columns:

* Math
* Science
* English

became row values under **Subject**, and their numbers became values under **Marks**.

---

## ☑️ Example 2: Monthly Sales

### 🔴 Wide Table

| Product | Jan | Feb | Mar |
| ------- | --- | --- | --- |
| Pen     | 120 | 140 | 135 |
| Pencil  | 200 | 210 | 220 |

### 🔴 Long Table after Unpivot

| Product | Month | Sales |
| ------- | ----- | ----- |
| Pen     | Jan   | 120   |
| Pen     | Feb   | 140   |
| Pen     | Mar   | 135   |
| Pencil  | Jan   | 200   |
| Pencil  | Feb   | 210   |
| Pencil  | Mar   | 220   |

Here:

* Jan, Feb, Mar became row entries in **Month**
* values became **Sales**

---

## ☑️ General Pattern of Unpivot

Suppose wide table is:

| ID | A  | B  | C  |
| -- | -- | -- | -- |
| 1  | 10 | 20 | 30 |

After unpivot:

| ID | Variable | Value |
| -- | -------- | ----- |
| 1  | A        | 10    |
| 1  | B        | 20    |
| 1  | C        | 30    |

---

# ✅ 6) Pivot: Long to Wide

## ☑️ Definition

Pivot takes row values from one column and turns them into separate columns.

---

## ☑️ Example 1: Student Marks

### 🔴 Long Table

| StudentID | Name | Subject | Marks |
| --------- | ---- | ------- | ----- |
| 101       | Asha | Math    | 85    |
| 101       | Asha | Science | 90    |
| 101       | Asha | English | 88    |
| 102       | Ravi | Math    | 78    |
| 102       | Ravi | Science | 82    |
| 102       | Ravi | English | 80    |

### 🔴 After Pivot

| StudentID | Name | Math | Science | English |
| --------- | ---- | ---- | ------- | ------- |
| 101       | Asha | 85   | 90      | 88      |
| 102       | Ravi | 78   | 82      | 80      |

### 🔴 What happened?

The values from **Subject** became column headers:

* Math
* Science
* English

The values from **Marks** filled those columns.

---

## ☑️ Example 2: Product Sales

### 🔴 Long Table

| Product | Month | Sales |
| ------- | ----- | ----- |
| Pen     | Jan   | 120   |
| Pen     | Feb   | 140   |
| Pen     | Mar   | 135   |
| Pencil  | Jan   | 200   |
| Pencil  | Feb   | 210   |
| Pencil  | Mar   | 220   |

### 🔴 After Pivot

| Product | Jan | Feb | Mar |
| ------- | --- | --- | --- |
| Pen     | 120 | 140 | 135 |
| Pencil  | 200 | 210 | 220 |

---

# ✅ 7) Pivot vs Unpivot at a Glance

| Feature      | Pivot                         | Unpivot                        |
| ------------ | ----------------------------- | ------------------------------ |
| Direction    | Long → Wide                   | Wide → Long                    |
| Converts     | Row values into columns       | Columns into rows              |
| Best for     | Reports, summaries, crosstabs | Analysis, cleaning, dashboards |
| Output shape | More columns, fewer rows      | Fewer columns, more rows       |

---

# ✅ 8) Step-by-Step Logic

## ☑️ A) How Unpivot works

Suppose you have:

| EmpID | Q1 | Q2 | Q3 |
| ----- | -- | -- | -- |
| E1    | 10 | 20 | 30 |

You choose:

* **identifier column**: EmpID
* **value columns**: Q1, Q2, Q3

Result:

| EmpID | Quarter | Value |
| ----- | ------- | ----- |
| E1    | Q1      | 10    |
| E1    | Q2      | 20    |
| E1    | Q3      | 30    |

So each original value column becomes a row.

---

## ☑️ B) How Pivot works

Suppose you have:

| EmpID | Quarter | Value |
| ----- | ------- | ----- |
| E1    | Q1      | 10    |
| E1    | Q2      | 20    |
| E1    | Q3      | 30    |

You choose:

* row identifier = EmpID
* columns = Quarter
* values = Value

Result:

| EmpID | Q1 | Q2 | Q3 |
| ----- | -- | -- | -- |
| E1    | 10 | 20 | 30 |

---

# ✅ 9) Important Terms

## ☑️ Identifier columns

Columns that uniquely describe the entity and should remain unchanged during unpivot.

Examples:

* StudentID
* Name
* Product
* EmployeeID

## ☑️ Attribute column

The new column created from former headers during unpivot.

Examples:

* Subject
* Month
* Quarter

## ☑️ Value column

The new column that stores actual data values.

Examples:

* Marks
* Sales
* Revenue

---

# ✅ 10) Real-Life Use Cases

## ☑️ Unpivot use cases

### 🔴 Example:

An Excel sheet has columns:

* Jan Sales
* Feb Sales
* Mar Sales
* Apr Sales

To make a line chart by month, it is often better to unpivot into:

| Product | Month | Sales |

This makes filtering and charting easier.

---

## ☑️ Pivot use cases

### 🔴 Example:

You have transaction-level data:

| Product | Region | Sales |

You want a report like:

| Product | East | West | North | South |

This needs pivot.

---

# ✅ 11) Example with Employee Attendance

## ☑️ Wide Format

| EmpID | Name | Mon | Tue | Wed |
| ----- | ---- | --- | --- | --- |
| E101  | Amit | P   | A   | P   |
| E102  | Rina | P   | P   | P   |

## ☑️ Unpivoted Long Format

| EmpID | Name | Day | Status |
| ----- | ---- | --- | ------ |
| E101  | Amit | Mon | P      |
| E101  | Amit | Tue | A      |
| E101  | Amit | Wed | P      |
| E102  | Rina | Mon | P      |
| E102  | Rina | Tue | P      |
| E102  | Rina | Wed | P      |

## ☑️ Pivot back to Wide

| EmpID | Name | Mon | Tue | Wed |
| ----- | ---- | --- | --- | --- |
| E101  | Amit | P   | A   | P   |
| E102  | Rina | P   | P   | P   |

---

# ✅ 12) Example with Survey Data

## ☑️ Wide Format

| RespondentID | EaseOfUse | Support | Pricing |
| ------------ | --------- | ------- | ------- |
| 1            | 4         | 5       | 3       |
| 2            | 5         | 4       | 2       |

## ☑️ After Unpivot

| RespondentID | Question  | Rating |
| ------------ | --------- | ------ |
| 1            | EaseOfUse | 4      |
| 1            | Support   | 5      |
| 1            | Pricing   | 3      |
| 2            | EaseOfUse | 5      |
| 2            | Support   | 4      |
| 2            | Pricing   | 2      |

This long format is better for:

* average rating by question
* plotting
* analysis

---

# ✅ 13) One Important Note: Pivot May Need Aggregation

Sometimes pivoting is not straightforward.

## ☑️ Example Long Table

| Product | Month | Sales |
| ------- | ----- | ----- |
| Pen     | Jan   | 100   |
| Pen     | Jan   | 50    |

If you pivot directly, there are **two values** for:

* Product = Pen
* Month = Jan

So pivot must decide what to do:

* Sum
* Average
* Count
* Max
* Min

### 🔴 Pivot with Sum

| Product | Jan |
| ------- | --- |
| Pen     | 150 |

So when duplicate combinations exist, **pivot usually requires aggregation**.

---

# ✅ 14) Unpivot Usually Does Not Aggregate

Unpivot normally just reshapes data.

It does not sum, average, or combine values.

It simply converts selected columns into rows.

---

# ✅ 15) Excel Perspective

## ☑️ Unpivot in Excel / Power Query

Usually done using:

* **Power Query**
* select identifier columns
* choose **Unpivot Other Columns** or **Unpivot Columns**

### 🔴 Example

If the table is:

| Product | Jan | Feb | Mar |

You keep `Product` fixed and unpivot Jan, Feb, Mar.

You get:

| Product | Attribute | Value |

Then rename:

* Attribute → Month
* Value → Sales

---

## ☑️ Pivot in Excel

Usually done using:

* **PivotTable**
* or Power Query Pivot Column

In a PivotTable:

* Rows area = identifier
* Columns area = category
* Values area = numeric field

---

# ✅ 16) SQL Perspective

## ☑️ Unpivot concept in SQL

Some SQL systems support `UNPIVOT`, but often it is done using `UNION ALL`.

### 🔴 Example concept

Wide table:

| ID | Jan | Feb |
| -- | --- | --- |
| 1  | 100 | 120 |

Converted to:

| ID | Month | Sales |
| -- | ----- | ----- |
| 1  | Jan   | 100   |
| 1  | Feb   | 120   |

---

## ☑️ Pivot concept in SQL

Many SQL systems use `PIVOT`, or conditional aggregation.

Example idea:

* group by ID
* create columns for Jan, Feb, Mar

---

# ✅ 17) Pandas Perspective

## ☑️ Unpivot in pandas

Usually done with `melt()`

Example concept:

* `id_vars` = columns to keep fixed
* `value_vars` = columns to unpivot

## ☑️ Pivot in pandas

Usually done with:

* `pivot()`
* `pivot_table()`

`pivot_table()` is used when aggregation is needed.

---

# ✅ 18) Power BI / Power Query Perspective

In Power Query:

* **Unpivot Columns**
* **Unpivot Other Columns**
* **Pivot Column**

This is extremely common during data cleaning.

### 🔴 Typical pattern

Raw imported file:

* Month names across columns
* multiple score columns
* repeated yearly columns

You unpivot first, then create visuals more easily.

---

# ✅ 19) Common Mistakes

## ☑️ Mistake 1: Choosing wrong identifier columns

If you unpivot the wrong columns, important context may be lost.

### 🔴 Example

If `Name` should remain fixed but is also unpivoted, the result becomes messy.

---

## ☑️ Mistake 2: Pivoting data with duplicates without aggregation

If one row-key and one column-key combination has multiple records, simple pivot fails or gives unexpected results.

---

## ☑️ Mistake 3: Thinking pivot and PivotTable are exactly the same

They are related, but:

* **pivot operation** = reshape data
* **PivotTable** = reporting and summarization tool

---

## ☑️ Mistake 4: Not renaming Attribute and Value

After unpivot, generic names like:

* Attribute
* Value

should often be renamed to meaningful names such as:

* Month
* Sales
* Subject
* Marks

---

# ✅ 20) How to Decide Whether to Pivot or Unpivot

Ask these questions:

## ☑️ Use Unpivot if:

* Do I have repeated information across many columns?
* Do I want one category column and one value column?
* Do I want easier analysis, filtering, charting?

## ☑️ Use Pivot if:

* Do I want categories shown as separate columns?
* Do I want a report-like matrix?
* Do I need summary view by row and column groups?

---

# ✅ 21) Best Simple Memory Trick

### 🔴 Unpivot

**Columns become rows**

### 🔴 Pivot

**Rows become columns**

Or even simpler:

* **Wide → Long = Unpivot**
* **Long → Wide = Pivot**

---

# ✅ 22) Full End-to-End Example

## ☑️ Step 1: Wide Table

| Region | Q1 | Q2 | Q3 | Q4 |
| ------ | -- | -- | -- | -- |
| East   | 10 | 20 | 30 | 40 |
| West   | 15 | 25 | 35 | 45 |

---

## ☑️ Step 2: Unpivot to Long

| Region | Quarter | Revenue |
| ------ | ------- | ------- |
| East   | Q1      | 10      |
| East   | Q2      | 20      |
| East   | Q3      | 30      |
| East   | Q4      | 40      |
| West   | Q1      | 15      |
| West   | Q2      | 25      |
| West   | Q3      | 35      |
| West   | Q4      | 45      |

---

## ☑️ Step 3: Pivot back to Wide

| Region | Q1 | Q2 | Q3 | Q4 |
| ------ | -- | -- | -- | -- |
| East   | 10 | 20 | 30 | 40 |
| West   | 15 | 25 | 35 | 45 |

So pivot and unpivot are reverse-type reshape operations.

---

# ✅ 23) Summary

## ☑️ Unpivot

* converts wide data to long data
* changes multiple columns into rows
* creates an attribute column and a value column
* useful for cleaning and analysis

## ☑️ Pivot

* converts long data to wide data
* changes row values into columns
* may require aggregation if duplicates exist
* useful for reports and summaries

---

# ✅ 24) Final Comparison Example

## ☑️ Wide

| ID | Jan | Feb | Mar |
| -- | --- | --- | --- |
| A  | 10  | 20  | 30  |

## ☑️ Unpivot

| ID | Month | Sales |
| -- | ----- | ----- |
| A  | Jan   | 10    |
| A  | Feb   | 20    |
| A  | Mar   | 30    |

## ☑️ Pivot back

| ID | Jan | Feb | Mar |
| -- | --- | --- | --- |
| A  | 10  | 20  | 30  |

---

# ✅ 25) One-Line Conclusion

**Unpivot transforms wide tables into long tables by turning columns into rows, while pivot transforms long tables into wide tables by turning row values into columns.**

---

