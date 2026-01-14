# 📝 EDA Module 1 Reviewer / Cheat Sheet

## 1. The "Golden" Formulas

**Variance Shortcut:**
$$V(X) = E[X^2] - (E[X])^2$$
_Always calculate $E[X]$ and $E[X^2]$ separately._

**Standard Deviation:**
$$\sigma = \sqrt{V(X)}$$

**Covariance:**
$$Cov(X, Y) = E[XY] - E[X]E[Y]$$

---

## 2. Discrete vs. Continuous (Side-by-Side)

| Feature         | Discrete (Countable)            | Continuous (Measured)                       |
| :-------------- | :------------------------------ | :------------------------------------------ |
| **Function**    | **PMF** $p(x)$                  | **PDF** $f(x)$                              |
| **Total Prob**  | $\sum_{\text{all } x} p(x) = 1$ | $\int_{-\infty}^{\infty} f(x) dx = 1$       |
| **Probability** | $P(X=x) = p(x)$                 | $P(X=x) = 0$ (Point prob is 0)              |
| **Interval**    | Sum values in range             | $\int_{a}^{b} f(x) dx$                      |
| **CDF $F(x)$**  | $\sum_{t \le x} p(t)$           | $\int_{-\infty}^{x} f(t) dt$                |
| **Mean $E[X]$** | $\sum x \cdot p(x)$             | $\int_{-\infty}^{\infty} x \cdot f(x) dx$   |
| **$E[X^2]$**    | $\sum x^2 \cdot p(x)$           | $\int_{-\infty}^{\infty} x^2 \cdot f(x) dx$ |

---

## 3. Joint Distributions (2 Variables)

### Marginal Distribution (Getting rid of one variable)

- **To find X:** Sum/Integrate out **Y**.
  - _Discrete:_ $p_X(x) = \sum_{\text{all } y} p(x,y)$
  - _Continuous:_ $f_X(x) = \int_{-\infty}^{\infty} f(x,y) dy$

### Conditional Distribution

$$f(x|y) = \frac{f(x,y)}{f_Y(y)}$$
_Note: The denominator is the Marginal of the "given" variable._

### Independence Check

Variables $X$ and $Y$ are independent if:
$$f(x,y) = f_X(x) \cdot f_Y(y)$$
_If independent, Covariance is ALWAYS 0._

---

## 4. Common Distributions

### Discrete

1.  **Binomial ($n, p$):** Number of successes in $n$ trials.
    - $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$
    - $\mu = np$, $\sigma^2 = np(1-p)$
2.  **Poisson ($\lambda$):** Number of events in a fixed interval.
    - $P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}$
    - $\mu = \lambda$, $\sigma^2 = \lambda$

### Continuous

1.  **Uniform ($a, b$):** Flat probability.
    - $f(x) = \frac{1}{b-a}$
    - $\mu = \frac{a+b}{2}$
2.  **Exponential ($\lambda$):** Time until first event (Memoryless).
    - $f(x) = \lambda e^{-\lambda x}$ (for $x > 0$)
    - $F(x) = 1 - e^{-\lambda x}$
    - $\mu = \frac{1}{\lambda}$, $\sigma^2 = \frac{1}{\lambda^2}$
3.  **Normal ($\mu, \sigma$):** The Bell Curve.
    - Standardize to Z: $Z = \frac{X - \mu}{\sigma}$

---

## 5. Calculus Reminders for EDA

**Integration by Parts (LIATE):**
Used for $E[X]$ in Exponential distributions.
$$\int u \, dv = uv - \int v \, du$$
_Tip: Let $u = x$ and $dv = e^{-\lambda x} dx$_

**Double Integrals:**
$$\int_{0}^{1} \int_{0}^{y} f(x,y) dx dy$$
_Always do the INNER integral first (treat outer variable as constant)._
