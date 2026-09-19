Task 12 – Missing Value Identification

Project Overview

This project focuses on identifying and summarizing missing values in the Iris dataset.

The analysis was performed using Excel and Python with Pandas.

Objective

The objective of this task is to:

- Identify missing values in the dataset.
- Count missing values for each column.
- Summarize where missing values occur.
- Understand why missing values should not be removed without justification.

Dataset

Dataset: Iris Dataset

Rows: 150

Columns analyzed:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
- Species

Tools Used

- Microsoft Excel
- Python
- Pandas
- Scikit-learn

Methodology

Excel

The dataset was inspected in Excel using the "COUNTBLANK" function to count missing values in each column.

Python

The Iris dataset was loaded using Scikit-learn and converted into a Pandas DataFrame.

The following Pandas method was used:

df.isnull().sum()

This was used to calculate the number of missing values in each column.

Missing Value Summary

Column| Missing Values
Sepal Length| 0
Sepal Width| 0
Petal Length| 0
Petal Width| 0
Species| 0

Findings

The analysis found no missing values in the Iris dataset. All analyzed columns contained complete data.

Since there were no missing values, no rows or values were removed or replaced.

Key Learning

Missing values should be inspected before performing data analysis or modeling. Blindly deleting rows can result in loss of useful information and may affect the analysis.

Conclusion

The Iris dataset was successfully checked for missing values using both Excel and Python Pandas. The dataset contained zero missing values, so no missing-value treatment was required.

Project Files

- "Task_12_Missing_Values.py" – Python/Pandas analysis
- "Task_12_Missing_Value_Identification.xlsx" – Excel missing-value summary
- "README.md" – Project documentation
- "Rollback_Evidence/" – Version/rollback evidence
