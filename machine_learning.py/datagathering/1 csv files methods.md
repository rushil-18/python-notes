# Pandas — Data Loading & Preprocessing for Machine Learning

> Notes for the Machine Learning / scikit-learn learning track.

---

# 1. Loading CSV Files

```python
import pandas as pd

df = pd.read_csv("placement.csv")
```

## Basic inspection

```python
df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

Before preprocessing, always understand what you loaded.

---

# 2. Important `read_csv()` Parameters

## `sep`

Used when the separator is not a comma.

```python
df = pd.read_csv("data.txt", sep="\t")
```

Example: tab-separated values.

---

## `names`

Create column names when the dataset does not contain headers.

```python
df = pd.read_csv(
    "data.csv",
    names=["name", "age", "salary"]
)
```

If the file already has a header, be careful: using `names` changes how the header is interpreted.

---

## `index_col`

Use a column as the DataFrame index.

```python
df = pd.read_csv(
    "data.csv",
    index_col="id"
)
```

---

## `header`

Specify which row contains the column names.

```python
df = pd.read_csv(
    "data.csv",
    header=1
)
```

This uses row 1 as the header.

---

## `usecols`

Load only selected columns.

```python
df = pd.read_csv(
    "data.csv",
    usecols=["name", "salary"]
)
```

> Correct parameter: `usecols`, not `use_columns`.

---

## `skiprows`

Skip rows while loading.

```python
df = pd.read_csv(
    "data.csv",
    skiprows=[0, 1]
)
```

Or:

```python
df = pd.read_csv(
    "data.csv",
    skiprows=5
)
```

This skips the first 5 rows.

---

## `nrows`

Load only a specific number of rows.

```python
df = pd.read_csv(
    "data.csv",
    nrows=100
)
```

Useful for testing large datasets.

---

# 3. Encoding

If a CSV contains characters that cannot be decoded using the default encoding, you may get:

```text
UnicodeDecodeError
```

Specify the appropriate encoding:

```python
df = pd.read_csv(
    "data.csv",
    encoding="latin-1"
)
```

Common encodings include:

```python
encoding="utf-8"
encoding="latin-1"
encoding="cp1252"
```

Do not automatically assume `latin-1`; determine the actual encoding when possible.

---

# 4. Handling Bad Rows

Older tutorials may show:

```python
error_bad_lines=False
```

This is outdated.

Use:

```python
df = pd.read_csv(
    "data.csv",
    on_bad_lines="skip"
)
```

Options:

```python
on_bad_lines="error"
on_bad_lines="warn"
on_bad_lines="skip"
```

- `error` → raise an error
- `warn` → skip bad lines and warn
- `skip` → skip bad lines

---

# 5. `dtype`

Specify the data type of a column while loading.

```python
df = pd.read_csv(
    "data.csv",
    dtype={"age": "int64"}
)
```

Or:

```python
dtype={"age": int}
```

---

# 6. Dates

Parse date columns while loading:

```python
df = pd.read_csv(
    "data.csv",
    parse_dates=["date"]
)
```

Or convert later:

```python
df["date"] = pd.to_datetime(df["date"])
```

Then extract date information:

```python
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["day_name"] = df["date"].dt.day_name()
```

---

# 7. `converters`

Apply a function to values in a specific column while reading.

```python
def rename(name):
    if name == "Royal Challengers Bangalore":
        return "RCB"
    return name
```

Then:

```python
df = pd.read_csv(
    "data.csv",
    converters={"team": rename}
)
```

> Correct parameter: `converters`, not `convertors`.

---

# 8. Missing-Value Representations

Datasets may represent missing values using:

```text
?
-
NA
N/A
unknown
$
```

Tell Pandas to treat them as missing:

```python
df = pd.read_csv(
    "data.csv",
    na_values=["?", "-", "NA", "N/A"]
)
```

Pandas will interpret those values as `NaN`.

---

# 9. Loading Large Datasets in Chunks

For very large datasets:

```python
dfs = pd.read_csv(
    "huge.csv",
    chunksize=5000
)
```

Then:

```python
for chunk in dfs:
    print(chunk.shape)
```

Each `chunk` is a DataFrame containing up to 5,000 rows.

---

# 10. Inspecting Missing Values

Check missing values:

```python
df.isna()
```

or:

```python
df.isnull()
```

Count missing values per column:

```python
df.isna().sum()
```

Percentage of missing values:

```python
df.isna().mean() * 100
```

---

# 11. Removing Missing Values

Remove rows containing missing values:

```python
df.dropna()
```

Remove rows when a specific column is missing:

```python
df.dropna(subset=["salary"])
```

Remove columns containing missing values:

```python
df.dropna(axis=1)
```

> Do not blindly remove missing data. Check how much information you would lose first.

---

# 12. Filling Missing Values

## Fill with a constant

```python
df["city"] = df["city"].fillna("Unknown")
```

## Numerical column — mean

```python
df["age"] = df["age"].fillna(df["age"].mean())
```

## Numerical column — median

```python
df["salary"] = df["salary"].fillna(df["salary"].median())
```

Median is often useful when outliers are present.

## Categorical column — mode

```python
df["city"] = df["city"].fillna(df["city"].mode()[0])
```

---

# 13. Duplicate Values

Check duplicate rows:

```python
df.duplicated()
```

Count duplicates:

```python
df.duplicated().sum()
```

Remove duplicates:

```python
df = df.drop_duplicates()
```

Only consider selected columns:

```python
df = df.drop_duplicates(
    subset=["name", "email"]
)
```

Control which duplicate to keep:

```python
df.drop_duplicates(keep="first")
df.drop_duplicates(keep="last")
df.drop_duplicates(keep=False)
```

`keep=False` removes all occurrences of duplicated rows.

---

# 14. Converting `object` to Numeric

A numerical column may sometimes be loaded as `object`.

Example:

```text
"50000"
"60000"
"75000"
```

Check:

```python
df["salary"].dtype
```

Convert:

```python
df["salary"] = pd.to_numeric(df["salary"])
```

If invalid values may exist:

```python
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)
```

Invalid values become `NaN`.

---

# 15. `astype()`

Use when you know the conversion is valid:

```python
df["age"] = df["age"].astype(int)
```

```python
df["age"] = df["age"].astype(float)
```

```python
df["category"] = df["category"].astype("string")
```

### Difference

Use `astype()` when the conversion is known to be valid.

Use:

```python
pd.to_numeric(..., errors="coerce")
```

when the column may contain invalid values.

---

# 16. Removing Unwanted Characters

Example:

```text
₹50,000
₹60,000
₹75,000
```

Remove currency symbol:

```python
df["salary"] = df["salary"].str.replace(
    "₹", "",
    regex=False
)
```

Remove commas:

```python
df["salary"] = df["salary"].str.replace(
    ",", "",
    regex=False
)
```

Convert to numeric:

```python
df["salary"] = pd.to_numeric(df["salary"])
```

Result:

```text
50000
60000
75000
```

---

# 17. Removing Multiple Characters with Regex

Example:

```text
"$50,000"
"$60,000"
"$70,000"
```

Use:

```python
df["salary"] = df["salary"].str.replace(
    r"[$,]",
    "",
    regex=True
)
```

Then:

```python
df["salary"] = pd.to_numeric(df["salary"])
```

---

# 18. Removing Whitespace

Example:

```text
" Delhi"
"Delhi "
"  Delhi  "
```

Use:

```python
df["city"] = df["city"].str.strip()
```

Other methods:

```python
df["city"].str.lstrip()
df["city"].str.rstrip()
```

---

# 19. Standardizing Text

Example:

```text
Male
male
MALE
M
```

Convert to lowercase:

```python
df["gender"] = df["gender"].str.lower()
```

Strip whitespace and lowercase:

```python
df["gender"] = (
    df["gender"]
    .str.strip()
    .str.lower()
)
```

Map inconsistent values:

```python
df["gender"] = df["gender"].replace({
    "m": "male",
    "f": "female"
})
```

---

# 20. `replace()`

Useful for cleaning categorical data:

```python
df["gender"] = df["gender"].replace({
    "M": "Male",
    "m": "Male",
    "F": "Female",
    "f": "Female"
})
```

Replace arbitrary values:

```python
df = df.replace("-", np.nan)
```

---

# 21. Unique Values

Find unique values:

```python
df["gender"].unique()
```

Count unique values:

```python
df["gender"].nunique()
```

Frequency of each value:

```python
df["gender"].value_counts()
```

This is extremely useful for discovering inconsistent categorical values.

---

# 22. Detecting Invalid / Impossible Values

Pandas does not automatically know that a value is logically wrong.

Example:

```text
age = 500
```

Inspect:

```python
df["age"].describe()
```

Filter suspicious values:

```python
df[df["age"] > 100]
```

```python
df[df["age"] < 0]
```

Depending on the situation, you can:

- Correct the value
- Remove the row
- Replace with `NaN`
- Investigate the source

---

# 23. Filtering Bad Rows

Example:

```python
df = df[df["age"] >= 18]
```

Multiple conditions:

```python
df = df[
    (df["age"] >= 18) &
    (df["salary"] > 0)
]
```

---

# 24. Rename Columns

Example:

```text
Student Name
Student Age
Placement Status
```

Rename:

```python
df = df.rename(columns={
    "Student Name": "student_name",
    "Student Age": "student_age",
    "Placement Status": "placement_status"
})
```

Normalize all column names:

```python
df.columns = (
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)
```

---

# 25. Drop Unnecessary Columns

```python
df = df.drop(columns=["id"])
```

Multiple columns:

```python
df = df.drop(
    columns=["id", "timestamp"]
)
```

---

# 26. Reset the Index

After deleting rows, you may get an index like:

```text
0
1
4
7
9
```

Reset it:

```python
df = df.reset_index(drop=True)
```

Result:

```text
0
1
2
3
4
```

---

# 27. Check Data Types

```python
df.dtypes
```

Detailed information:

```python
df.info()
```

Numeric columns:

```python
df.select_dtypes(include="number")
```

Object/text columns:

```python
df.select_dtypes(include="object")
```

Note: newer Pandas versions can use dedicated `string` dtypes, so not every text column will necessarily be `object`.

---

# 28. `convert_dtypes()`

Let Pandas convert columns to appropriate nullable dtypes:

```python
df = df.convert_dtypes()
```

---

# 29. Handling Infinite Values

Check for infinity:

```python
import numpy as np

np.isinf(df["column"]).sum()
```

Replace infinity with `NaN`:

```python
df = df.replace(
    [np.inf, -np.inf],
    np.nan
)
```

Then handle the resulting missing values.

---

# 30. Outliers

A simple first inspection:

```python
df["salary"].describe()
```

IQR method:

```python
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

Find outliers:

```python
df[
    (df["salary"] < lower) |
    (df["salary"] > upper)
]
```

Outlier handling will be studied properly later with statistics and feature engineering.

---

# 31. Sampling

Take a random number of rows:

```python
df.sample(100)
```

Take approximately 10%:

```python
df.sample(frac=0.1)
```

Useful when experimenting with large datasets.

---

# 32. Useful String Operations

These are worth knowing:

```python
.str.strip()
.str.lstrip()
.str.rstrip()
.str.lower()
.str.upper()
.str.replace()
.str.contains()
.str.split()
.str.extract()
```

They are especially useful for cleaning messy text columns.

---

# 33. Useful Selection / Manipulation

```python
df.loc[]
df.iloc[]
df.drop()
df.rename()
```

Filtering:

```python
df[df["age"] > 18]
```

---

# 34. Important ML Data-Preprocessing Workflow

When receiving a new dataset, don't randomly clean columns.

Follow a process:

```text
RAW DATA
   ↓
Load dataset
   ↓
df.head()
df.shape
df.info()
df.describe()
   ↓
Understand columns
   ↓
Missing values?
   ↓
Duplicate values?
   ↓
Wrong data types?
   ↓
Inconsistent categories?
   ↓
Bad characters / whitespace?
   ↓
Invalid values?
   ↓
Outliers?
   ↓
Date/time problems?
   ↓
Remove unnecessary columns
   ↓
Feature engineering
   ↓
Clean DataFrame
   ↓
Separate X and y
   ↓
Train/Test Split
   ↓
ML Model
```

---

# 35. Most Important Pandas Commands for ML

You do NOT need to memorize every Pandas function.

## Inspection

```python
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.dtypes
df.columns
```

## Missing values

```python
df.isna()
df.isna().sum()
df.dropna()
df.fillna()
```

## Duplicates

```python
df.duplicated()
df.duplicated().sum()
df.drop_duplicates()
```

## Data types

```python
df.astype()
pd.to_numeric()
pd.to_datetime()
df.convert_dtypes()
```

## Strings

```python
.str.strip()
.str.lower()
.str.upper()
.str.replace()
.str.contains()
.str.split()
.str.extract()
```

## Categories

```python
.unique()
.nunique()
.value_counts()
.replace()
```

## Rows / columns

```python
.drop()
.rename()
.loc[]
.iloc[]
```

## Filtering

```python
df[df["age"] > 18]
```

## Dates

```python
.dt.year
.dt.month
.dt.day
.dt.day_name()
```

## Outliers

```python
.quantile()
.describe()
```

## Sampling

```python
.sample()
```

---

# Important: Pandas Preprocessing vs ML Preprocessing

There is a difference between **data cleaning with Pandas** and **ML preprocessing with scikit-learn**.

Pandas:

```python
df["age"] = df["age"].fillna(
    df["age"].median()
)
```

Later, in scikit-learn, you will learn:

```python
SimpleImputer()
StandardScaler()
OneHotEncoder()
Pipeline()
ColumnTransformer()
```

These are important because ML preprocessing must be designed carefully to avoid **data leakage**.

We will cover this when we reach the scikit-learn workflow.

---

# Outdated Syntax to Avoid

### Old

```python
error_bad_lines=False
```

### Current

```python
on_bad_lines="skip"
```

---

### Incorrect

```python
use_columns=[...]
```

### Correct

```python
usecols=[...]
```

---

### Old `squeeze` approach

Do not rely on:

```python
squeeze
```

to turn a CSV column into a Series.

Simply use:

```python
series = df["column_name"]
```

---

# Final Mental Model

Think of Pandas preprocessing as:

```text
                 DATASET
                    ↓
              UNDERSTAND IT
                    ↓
        ┌───────────┴───────────┐
        ↓                       ↓
    STRUCTURE                 VALUES
        ↓                       ↓
  wrong dtypes             missing values
  wrong columns            duplicates
  bad headers              bad characters
  unwanted columns         invalid values
                           outliers
        └───────────┬───────────┘
                    ↓
               CLEAN DATA
                    ↓
             FEATURE ENGINEERING
                    ↓
                 X + y
                    ↓
            MACHINE LEARNING
```

This is the preprocessing toolkit you should keep beside you while learning ML.
