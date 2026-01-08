# 📊 EDA Module 1 Exam Checklist

**Scope:** Intro to Data, Probability, Random Variables (Discrete/Continuous/Joint)

## 🛠️ Prerequisites (The "Hidden" Killers)

_If you can't do these, you can't solve Continuous or Joint RV problems._

- [ ] **Definite Integrals:** Calculating area under a curve (for Probabilities).
- [ ] **Improper Integrals:** Integrating from $0$ to $\infty$ (Crucial for Exponential Distributions).
- [ ] **Integration by Parts:** $\int x e^{-x} dx$ (REQUIRED for finding Expected Value $E[X]$).
- [ ] **Double Integrals:** $\int \int f(x,y) dx dy$ (REQUIRED for Joint Distributions).
- [ ] **Setting Bounds:** Determining limits of integration from a word problem (e.g., "$x < y$").
- [ ] **Summation Notation:** Understanding $\sum x p(x)$.

## 1️⃣ Introduction to Data Analysis

- [ ] **Data Types:** Nominal, Ordinal, Interval, Ratio.
- [ ] **Sampling:** Simple Random, Stratified, Systematic, Cluster.
- [ ] **Descriptive Stats:** Mean, Median, Mode, Variance, Standard Deviation.
- [ ] **Boxplots:** calculating IQR and identifying outliers ($1.5 \times IQR$).

## 2️⃣ Probability Foundations

- [ ] **Set Theory:** Union ($A \cup B$), Intersection ($A \cap B$), Complement ($A'$).
- [ ] **Axioms of Probability:** $P(S) = 1$, $0 \le P(E) \le 1$.
- [ ] **Conditional Probability:** $P(A|B) = P(A \cap B) / P(B)$.
- [ ] **Independence:** Checking if $P(A \cap B) = P(A)P(B)$.
- [ ] **Bayes' Theorem:** The "Tree Diagram" problems.

## 3️⃣ Random Variables (One Dimension)

### Discrete (The Summation World $\Sigma$)

- [ ] **PMF Properties:** $\sum p(x) = 1$.
- [ ] **CDF ($F(x)$):** Step functions (cumulative sum).
- [ ] **Expectation ($E[X]$):** $\sum x p(x)$.
- [ ] **Variance ($V[X]$):** $E[X^2] - (E[X])^2$.
- [ ] **Distributions:** Binomial, Poisson, Geometric, Hypergeometric.

### Continuous (The Integration World $\int$)

- [ ] **PDF Properties:** $\int_{-\infty}^{\infty} f(x) dx = 1$ (Often used to "Find constant $k$").
- [ ] **Probability as Area:** $P(a < X < b) = \int_{a}^{b} f(x) dx$.
- [ ] **CDF ($F(x)$):** $\int_{-\infty}^{x} f(t) dt$.
- [ ] **Expectation ($E[X]$):** $\int x f(x) dx$ (Use Integration by Parts!).
- [ ] **Distributions:** Uniform, Exponential, Normal (Gaussian).

## 4️⃣ Joint Probability Distributions (Two Dimensions)

_The hardest part of Module 1._

- [ ] **Joint PMF/PDF:** Checking if $\sum \sum p(x,y) = 1$ or $\iint f(x,y) dy dx = 1$.
- [ ] **Marginal Distributions:** Integrating out the "other" variable ($g(x) = \int f(x,y) dy$).
- [ ] **Conditional Distributions:** $f(x|y) = f(x,y) / h(y)$.
- [ ] **Independence:** Does $f(x,y) = g(x)h(y)$?
- [ ] **Covariance:** $E[XY] - E[X]E[Y]$.
- [ ] **Correlation Coefficient:** $\rho = Cov(X,Y) / (\sigma_x \sigma_y)$.
