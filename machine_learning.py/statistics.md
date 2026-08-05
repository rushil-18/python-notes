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

3. PROBABILITY DISTRIBUTION - 
      Is there only ONE trial?

                           Yes
                            │
                     Bernoulli Distribution
                            │
               (Success / Failure)

---------------------------------------------------

                Multiple independent trials?

                           Yes
                            │
                     Binomial Distribution
                            │
          (Count the number of successes)

---------------------------------------------------

          Are all outcomes equally likely?

                           Yes
                            │
                     Uniform Distribution
                            │
        (Fair die, random number generator)

---------------------------------------------------

     Counting events in a fixed time/space interval?

                           Yes
                            │
                     Poisson Distribution
                            │
      (Emails/hour, customers/minute, calls/day)

---------------------------------------------------

     Real-valued natural measurements?

                           Yes
                            │
                     Normal Distribution
                            │
        (Height, Weight, IQ, Exam Scores...)



NORMAL DISTIBUTION - 
BELL CURVE 


4. INFERENTIAL STATISTICS
Sampling

Sampling is simply:

Selecting a subset from a population.

Good sampling should represent the population well.
Types of Sampling
1. Random Sampling ⭐⭐⭐⭐⭐

Every individual has an equal chance of being selected.

Example:

A lottery.

2. Stratified Sampling ⭐⭐⭐⭐

Divide the population into groups (strata), then sample from each.

Example:

University:

CSE

ECE

ME

Civil

Take students from every department.

This is very common in ML because it preserves class balance.

3. Systematic Sampling

Pick every kth person.

Example:

Every 10th customer entering a store.

4. Cluster Sampling

Randomly choose entire groups.

Example:

Instead of selecting students individually, randomly choose 5 classrooms and survey everyone in those classrooms.


*CENTERAL LIMIT THEOREM*
1. Central Limit Theorem (CLT) ⭐⭐⭐⭐⭐
Definition

Regardless of the original population distribution, the distribution of sample means approaches a normal distribution as the sample size becomes sufficiently large.

Conditions
Random sampling
Large sample size (typically n ≥ 30)
Important Point

CLT does NOT say:

❌ The original population becomes normal.

It says:

✅ The distribution of sample means becomes approximately normal.

Process
Population

↓

Take Random Sample

↓

Calculate Mean

↓

Repeat Many Times

↓

Distribution of Sample Means

↓

Approximately Normal
Why is CLT Important?

It allows us to:

Estimate population parameters
Build confidence intervals
Perform hypothesis testing
Make inferences from samples
ML Applications
A/B Testing
Model evaluation
Confidence intervals
Statistical inference
2. Confidence Interval (CI) ⭐⭐⭐⭐
Definition

A confidence interval is:

A range of values that is likely to contain the true population parameter.

Example

Sample Mean:

170 cm

95% Confidence Interval

168 cm – 172 cm

Interpretation:

We estimate that the true population mean lies between 168 cm and 172 cm.

Why do we need CI?

A sample mean is only an estimate.

Different samples produce different means.

Instead of reporting one number,

we report a range.

Effect of Sample Size

Large Sample

↓

Less Sampling Variability

↓

Narrow Confidence Interval

Small Sample

↓

More Sampling Variability

↓

Wide Confidence Interval

Important Fact

95% Confidence means:

If we repeatedly take samples and build confidence intervals, about 95% of those intervals will contain the true population parameter.

It does NOT mean:

❌ There is a 95% probability that the true mean is inside this specific interval.

ML Applications
A/B Testing
Accuracy estimation
Survey analysis
Business analytics
3. Hypothesis Testing ⭐⭐⭐⭐⭐
Purpose

To determine whether an observed difference is:

Real
Or due to random chance
Step 1

Form two hypotheses.

Null Hypothesis (H₀)

Default assumption.

Usually means:

No effect
No difference
No relationship

Examples

Medicine has no effect.

Advertisement does not increase sales.

New ML model is not better.
Alternative Hypothesis (H₁)

Opposite of H₀.

Means:

Effect exists
Difference exists
Relationship exists

Examples

Medicine works.

Advertisement increases sales.

New model performs better.
Courtroom Analogy

H₀

↓

Assume Innocent

↓

Collect Evidence

↓

Strong Evidence?

↓

Reject H₀

Otherwise

↓

Fail to Reject H₀

Decision

Reject H₀

↓

Enough evidence against H₀.

Fail to Reject H₀

↓

Not enough evidence against H₀.

Notice:

We never prove H₀ is true.

ML Applications
Comparing two ML models
A/B Testing
Feature significance
Medical trials
4. p-value ⭐⭐⭐⭐⭐
Definition

The p-value is:

The probability of observing results at least as extreme as those observed, assuming the null hypothesis is true.

Easy Meaning

A p-value measures

How surprising are my results if H₀ is actually true?

Think of it as a surprise meter.

Interpretation

Small p-value

↓

Results are very surprising under H₀.

↓

Reject H₀.

Large p-value

↓

Results are not surprising under H₀.

↓

Fail to Reject H₀.

Standard Decision Rule

Usually

α = 0.05

If

p < 0.05

↓

Reject H₀

If

p > 0.05

↓

Fail to Reject H₀

Coin Example

H₀:

Coin is fair.

Result

52 Heads

48 Tails

Not surprising

↓

Large p-value

↓

Fail to Reject H₀

Result

98 Heads

2 Tails

Very surprising

↓

Small p-value

↓

Reject H₀

Common Mistake

❌

p = 0.02

↓

There is a 98% chance H₀ is false.

Wrong.

Correct interpretation:

If H₀ were true, there is a 2% chance of obtaining results this extreme (or more extreme) due to random chance.

ML Applications
Feature selection
A/B Testing
Medical research
Scientific experiments
Comparing algorithms
🎯 Interview Cheat Sheet
Central Limit Theorem

↓

Sample Means become Normal

--------------------------

Confidence Interval

↓

Range likely containing the true population parameter

--------------------------

H₀

↓

No Effect / No Difference

--------------------------

H₁

↓

Effect Exists

--------------------------

p-value

↓

How surprising are the results if H₀ is true?

--------------------------

Small p (<0.05)

↓

Reject H₀

--------------------------

Large p (>0.05)

↓

Fail to Reject H₀
💡 One-line Memory Tricks
CLT → "Sample means become normal."
Confidence Interval → "Estimate with a range, not a single value."
Null Hypothesis (H₀) → "Assume nothing changed."
Alternative Hypothesis (H₁) → "Something changed."
p-value → "How surprising are these results if H₀ is true?"
