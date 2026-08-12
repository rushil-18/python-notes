# Loading CSV, JSON, and SQL Data into Pandas

> Goal: Get data from different sources into a Pandas DataFrame so that it can be inspected, cleaned, preprocessed, and eventually used for Machine Learning.

---

# 1. The Big Picture

Different data sources can be converted into a common structure:

```text
                    DATA SOURCES
                         |
        +----------------+----------------+
        |                |                |
        v                v                v
       CSV              JSON             SQL
        |                |                |
        v                v                v
  pd.read_csv()    pd.read_json()    SQL Query
        |                |                |
        +----------------+----------------+
                         |
                         v
                  PANDAS DATAFRAME
                         |
                         v
                     INSPECTION
                         |
                         v
                      CLEANING
                         |
                         v
               FEATURE ENGINEERING
                         |
                         v
                       X + y
                         |
                         v
                  TRAIN / TEST
                         |
                         v
                  SCIKIT-LEARN
                         |
                         v
                       MODEL
```

The important idea:

> The original source can be different, but once the data is in a DataFrame, most Pandas preprocessing operations are the same.

---

# 2. CSV → DataFrame

CSV is usually the simplest format.

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

Inspect:

```python
df.head()
df.shape
df.info()
```

---

# 3. JSON → DataFrame

## Simple JSON

Suppose `students.json` contains:

```json
[
    {
        "name": "Rahul",
        "age": 20,
        "cgpa": 8.2
    },
    {
        "name": "Arjun",
        "age": 21,
        "cgpa": 7.8
    }
]
```

Load it:

```python
import pandas as pd

df = pd.read_json("students.json")

df.head()
```

---

# 4. Nested JSON

JSON can contain nested objects.

Example:

```json
[
    {
        "name": "Rahul",
        "student": {
            "age": 20,
            "cgpa": 8.2
        }
    }
]
```

For nested JSON, use `json_normalize()`.

```python
import json
from pandas import json_normalize

with open("students.json") as f:
    data = json.load(f)

df = json_normalize(data)

df
```

The nested data can become columns such as:

```text
name    student.age    student.cgpa
Rahul       20             8.2
```

`json_normalize()` is especially useful for API responses because APIs frequently return nested JSON.

---

# 5. Python JSON/Object → DataFrame

If the JSON has already been loaded into a Python list of dictionaries:

```python
data = [
    {"name": "Rahul", "age": 20},
    {"name": "Arjun", "age": 21}
]

df = pd.DataFrame(data)
```

---

# 6. SQL → DataFrame

SQL is different from CSV and JSON.

A CSV/JSON file is usually a file.

SQL generally refers to data stored in a database such as:

```text
MySQL
PostgreSQL
SQLite
SQL Server
Oracle
```

The general workflow is:

```text
Database
    ↓
SQL Query
    ↓
Python
    ↓
Pandas DataFrame
```

Use:

```python
df = pd.read_sql(
    "SELECT * FROM students",
    connection
)
```

---

# 7. SQLite → DataFrame

SQLite is useful for learning because it does not require a separate database server.

Suppose:

```text
students.db
```

Connect:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("students.db")
```

Read a table:

```python
df = pd.read_sql(
    "SELECT * FROM students",
    conn
)

df.head()
```

Workflow:

```text
students.db
     ↓
SQLite connection
     ↓
SELECT * FROM students
     ↓
Pandas DataFrame
```

---

# 8. MySQL → DataFrame

For MySQL, you need a database connector.

One common approach is SQLAlchemy:

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://username:password@localhost/database_name"
)

df = pd.read_sql(
    "SELECT * FROM students",
    engine
)
```

---

# 9. PostgreSQL → DataFrame

Similarly:

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql+psycopg2://username:password@localhost/database_name"
)

df = pd.read_sql(
    "SELECT * FROM students",
    engine
)
```

---

# 10. You Don't Have to Load the Entire Database

One major advantage of SQL is that you can select exactly what you need.

Instead of:

```sql
SELECT * FROM students;
```

you can use:

```sql
SELECT name, age, cgpa
FROM students
WHERE cgpa > 8.0;
```

Then:

```python
df = pd.read_sql(query, engine)
```

This is especially important when a database contains millions of rows.

General idea:

```text
Large Database
      ↓
SQL filters / joins / aggregates data
      ↓
Only required data
      ↓
Pandas DataFrame
```

---

# 11. SQL JOIN → DataFrame

Suppose you have two tables.

## students

```text
student_id | name
-----------|------
1          | Rahul
2          | Arjun
3          | Priya
```

## placements

```text
student_id | company
-----------|---------
1          | Google
2          | Amazon
```

You can join them in SQL:

```sql
SELECT
    students.name,
    placements.company
FROM students
LEFT JOIN placements
ON students.student_id = placements.student_id;
```

Then:

```python
df = pd.read_sql(query, engine)
```

Result:

```text
name      company
--------  -------
Rahul     Google
Arjun     Amazon
Priya     NULL
```

---

# 12. Pandas `merge()`

If the data is already in DataFrames, you can perform the equivalent operation with Pandas:

```python
df = pd.merge(
    students,
    placements,
    on="student_id",
    how="left"
)
```

Common join types:

```python
how="inner"
how="left"
how="right"
how="outer"
```

General rule:

```text
Large data still in database
        ↓
Prefer SQL JOIN

Data already loaded into DataFrames
        ↓
Use pd.merge()
```

---

# 13. `.sql` Files

A `.sql` file is usually not the database itself.

It may contain SQL commands such as:

```sql
CREATE TABLE students (...);

INSERT INTO students VALUES (...);
INSERT INTO students VALUES (...);
```

You first need to execute the SQL script against a database.

For SQLite:

```python
import sqlite3

conn = sqlite3.connect("students.db")

with open("students.sql", "r") as file:
    sql_script = file.read()

conn.executescript(sql_script)
```

Then read the resulting table:

```python
import pandas as pd

df = pd.read_sql(
    "SELECT * FROM students",
    conn
)
```

Now the data is in a DataFrame.

---

# 14. Important Commands to Remember

## CSV

```python
df = pd.read_csv("data.csv")
```

## JSON

```python
df = pd.read_json("data.json")
```

## Nested JSON

```python
df = pd.json_normalize(data)
```

## Python list of dictionaries

```python
df = pd.DataFrame(data)
```

## SQL

```python
df = pd.read_sql(
    "SELECT * FROM table_name",
    connection
)
```

## SQLite

```python
import sqlite3

conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM table_name",
    conn
)
```

## Pandas merge

```python
df = pd.merge(
    df1,
    df2,
    on="id",
    how="left"
)
```

---

# 15. Data Source → Pandas Cheat Sheet

| Data source | Main approach |
|---|---|
| CSV | `pd.read_csv()` |
| JSON | `pd.read_json()` |
| Nested JSON | `pd.json_normalize()` |
| Python dictionaries | `pd.DataFrame()` |
| SQLite | `pd.read_sql()` |
| MySQL | SQLAlchemy + `pd.read_sql()` |
| PostgreSQL | SQLAlchemy + `pd.read_sql()` |
| SQL script (`.sql`) | Execute script → query database → DataFrame |

---

# 16. Mental Model

Do not try to memorize dozens of import methods.

Think:

> "My job is to get structured data into a DataFrame."

Once you have:

```python
df
```

you can use the same Pandas tools:

```python
df.head()
df.info()
df.isna()
df.dropna()
df.fillna()
df.drop_duplicates()
df.astype()
df.value_counts()
df.groupby()
df.merge()
```

regardless of whether the original data came from CSV, JSON, or SQL.

---

# 17. ML Workflow

The complete process will eventually look like:

```text
CSV / JSON / SQL / API
          ↓
    Pandas DataFrame
          ↓
      Inspect Data
          ↓
       Clean Data
          ↓
   Feature Engineering
          ↓
      X and y
          ↓
    Train/Test Split
          ↓
   ML Preprocessing
          ↓
     ML Algorithm
          ↓
     Train Model
          ↓
      Evaluate
          ↓
      Predictions
```

---

# Key Takeaway

### CSV

```python
pd.read_csv()
```

### JSON

```python
pd.read_json()
```

### Nested JSON

```python
pd.json_normalize()
```

### SQL

```python
pd.read_sql()
```

### Already have Python data

```python
pd.DataFrame()
```

Once everything becomes a DataFrame, your normal Pandas preprocessing workflow applies.
