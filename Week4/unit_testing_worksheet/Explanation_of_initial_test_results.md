# Explanation of Initial Test Results

I ran my initial tests using pytest on the book sales dataset, which contains 1,070 rows and 15 columns. Out of 19 tests, 16 passed and 3 failed.

The three failures were related to missing values. The `Book Name` column contains 23 missing values, `Publishing Year` contains one missing value, and `language_code` contains 53 missing values. These failures show that the dataset does not meet my initial expectation that these fields should be complete.

I kept the failing tests because they identify data quality issues that could affect further analysis. The other tests passed, confirming that the dataset has the expected structure, that selected columns have appropriate data types, that observed categories match the expected categories, that selected numerical values fall within the tested ranges, and that there are no duplicate rows.

My next step is to investigate how these missing values should be handled. I will avoid removing or replacing values without a clear reason, then rerun the tests to check whether any changes improve data quality without introducing new problems. 