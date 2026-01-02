# MATLAB Statistics Onramp Summary 📊

A quick reference guide for essential statistical commands used in Engineering Data Analysis (EDA). This covers data preparation, visualization, descriptive statistics, and hypothesis testing.

## 1. Import and Prepare Data

| Function      | Description                                                          |
| :------------ | :------------------------------------------------------------------- |
| `readtable`   | Create a table from a file (e.g., `.csv` or `.xlsx`).                |
| `categorical` | Convert a variable into a categorical type (essential for grouping). |

---

## 2. Visualizing Data 📈

| Function               | Example                         | Description                                                                                |
| :--------------------- | :------------------------------ | :----------------------------------------------------------------------------------------- |
| **`scatter`**          | `scatter(x,y)`                  | Create a scatter plot with circular markers at locations specified by vectors `x` and `y`. |
| **`gscatter`**         | `gscatter(x,y,g)`               | Create a scatter plot of `x` and `y`, grouped by `g` (adds color/legend auto-magically).   |
| **`histogram`**        | `histogram(x, 'BinWidth', 0.5)` | Create a histogram of `x` using a specific bin width (e.g., 0.5).                          |
| **`boxchart`**         | `boxchart(xgroup, ydata)`       | Create box plots of `ydata` grouped according to `xgroup`.                                 |
| **`scatterhistogram`** | `scatterhistogram(x,y)`         | Create a scatter plot of `x` and `y` with marginal histograms on the axes.                 |

---

## 3. Descriptive Statistics 🧮

### Measures of Center

| Function | Description                                                    |
| :------- | :------------------------------------------------------------- |
| `mean`   | Find the arithmetic average of the data.                       |
| `median` | Find the middle value of the sorted data (robust to outliers). |

### Measures of Spread

| Function | Description                                                             |
| :------- | :---------------------------------------------------------------------- |
| `std`    | Find the standard deviation (average distance from the mean).           |
| `range`  | Difference between the maximum and minimum values (`max - min`).        |
| `iqr`    | Interquartile Range: The range of the middle 50% of the data (Q3 - Q1). |

### Measures of Shape

| Function   | Description                                               |
| :--------- | :-------------------------------------------------------- |
| `skewness` | Determine if the data leans left or right (asymmetry).    |
| `kurtosis` | Determine the "tailedness" or peak intensity of the data. |

---

## 4. Normal Distributions 🔔

| Function  | Description                                                                                            |
| :-------- | :----------------------------------------------------------------------------------------------------- |
| `randn`   | Generate random numbers from the **standard** normal distribution ($\mu=0, \sigma=1$).                 |
| `normrnd` | Generate random numbers from a normal distribution with a known mean ($\mu$) and std dev ($\sigma$).   |
| `normpdf` | Return the **Probability Density Function (PDF)** value at `x` (height of the curve).                  |
| `normcdf` | Return the **Cumulative Distribution Function (CDF)** value at `x` (area under the curve to the left). |
| `fitdist` | Fit a specific probability distribution object to data.                                                |
| `qqplot`  | Display a Quantile-Quantile plot to visually check if data follows a normal distribution.              |

---

## 5. Hypothesis Testing 🧪

### Common Tests

| Function     | Description                                                                                |
| :----------- | :----------------------------------------------------------------------------------------- |
| `ttest2`     | Test for the difference in **means** between two independent populations.                  |
| `jbtest`     | Perform the **Jarque-Bera** test for normality (checks skewness/kurtosis matching normal). |
| `lillietest` | Perform the **Lilliefors** test for normality (robust for smaller samples).                |

### Selecting the Right Normality Test

| Test Name                      | MATLAB Function |
| :----------------------------- | :-------------- |
| **Jarque-Bera**                | `jbtest`        |
| **Lilliefors**                 | `lillietest`    |
| **Anderson-Darling**           | `adtest`        |
| **Chi-square goodness-of-fit** | `chi2gof`       |
| **Kolmogorov-Smirnov**         | `kstest`        |