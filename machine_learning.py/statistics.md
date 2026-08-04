Module 1: Descriptive Statistics
Mean
Median
Mode
Range
Variance
Standard Deviation
Quartiles
Percentiles
IQR
Outliers
Skewness
Kurtosis

Module 2: Probability
Sample Space
Events
Conditional Probability
Bayes Theorem
Random Variables

Module 3: Probability Distributions
Bernoulli
Binomial
Uniform
Normal
Poisson

Module 4: Inferential Statistics
Sampling
CLT
Confidence Intervals
Hypothesis Testing
p-values

Module 5: Statistics in ML
Correlation
Covariance
Feature Scaling
Bias-Variance
Evaluation Metrics


1. Mean (Average)
Definition
The average of all values.
Formula
Mean = Sum of all values / Number of values
When to use
Symmetric data
No significant outliers
Not good for
Salaries
House prices
Income
(outliers affect the mean)

np.mean(data)
df["column"].mean()

2. Median
Definition

The middle value after sorting.

Odd number of values

Take the middle value.

Example

2 4 6 8 10

Median = 6
Even number of values

Average of the two middle values.

2 4 6 8

Median = (4+6)/2 = 5
When to use
Outliers exist
Skewed data
Python
np.median(data)
df["column"].median()
3. Mode
Definition

The most frequently occurring value.

Example

2 3 3 4 5

Mode = 3
Types
Unimodal
Bimodal
Multimodal
No Mode
Best for

Categorical data.

Example

Gender

Male
Male
Female
Male

Mode = Male
Python
df["column"].mode()
Mean vs Median vs Mode
Measure	Meaning	Best Used For
Mean	Average	Symmetric numerical data
Median	Middle value	Data with outliers
Mode	Most frequent value	Categorical data
4. Variance
Definition

Average of squared distances from the mean.

Measures

Spread of data.

Interpretation

Small variance

↓

Values close together

Large variance

↓

Values far apart

Python
np.var(data)

df["column"].var()
5. Standard Deviation
Definition

Square root of variance.

Measures

Typical distance from the mean.

Interpretation

Small SD

↓

Less spread

Large SD

↓

More spread

Python
np.std(data)

df["column"].std()
6. Percentile
Meaning

Percentage of observations below a value.

Example

90th percentile

↓

90% of observations scored below you.

Percentage vs Percentile
Percentage	Percentile
Score out of total	Position among people
80/100 = 80%	Better than 80% of people
7. Quartiles

Divide data into four equal parts.

0%----25%----50%----75%----100%

      Q1     Q2     Q3

Q1

↓

25% below

Q2

↓

Median

Q3

↓

75% below

Finding Quartiles

Step 1

Sort data

↓

Step 2

Find median (Q2)

↓

Step 3

Split lower and upper halves

↓

Step 4

Median of lower half = Q1

↓

Median of upper half = Q3

8. IQR
Formula
IQR = Q3 − Q1

Measures

Middle 50% spread.

Used for

Boxplots
Outlier Detection
9. Outlier

An unusually large or small value.

Example

10
12
13
15
500

500 is an outlier.

Boxplot Rule
Lower Limit

Q1 − 1.5(IQR)

Upper Limit

Q3 + 1.5(IQR)

Anything outside these limits is considered an outlier.

Interview Cheat Sheet
Use	                Statistic
Average	               Mean
Outliers present	   Median
Categorical data	   Mode
Spread	               Variance
Human interpretation
of spread	           Standard Deviation

Position in dataset	   Percentile
Middle 50% spread	   IQR

10. Skewness 
is data symettric
if no skew then it is symetric meaning mean = median = mode (approx)

right skew - positive skew mode < median < mean
effected by more positive outliers 

left skew - mean < median < mode

11. High Kurtosis

↓

More extreme values

More outliers

Low Kurtosis

↓

Fewer extreme values

Less outlier-prone

Python
df.skew()

df.kurt()

or

from scipy.stats import skew, kurtosis

