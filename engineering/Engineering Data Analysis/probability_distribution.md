# 📊 Probability Distributions & Random Variables Reviewer

## 1. Core Concepts: The Language of Probability

| Concept                     | Discrete (Countable)                        | Continuous (Measurable)                               |
| :-------------------------- | :------------------------------------------ | :---------------------------------------------------- |
| **Random Variable (RV)**    | $X$ takes specific values (e.g., $0, 1, 2$) | $X$ takes any value in an interval (e.g., $1.532...$) |
| **Probability Function**    | **PMF** $p(x) = P(X=x)$                     | **PDF** $f(x)$ (Not a probability itself!)            |
| **Normalization**           | $\sum p(x) = 1$                             | $\int_{-\infty}^{\infty} f(x) dx = 1$                 |
| **CDF ($F(x)$)**            | $P(X \le x) = \sum_{t \le x} p(t)$          | $P(X \le x) = \int_{-\infty}^{x} f(t) dt$             |
| **Expected Value** ($E[X]$) | $\sum x \cdot p(x)$                         | $\int x \cdot f(x) dx$                                |

---

## 2. Discrete Distributions (The "Counters")

### 🟢 Bernoulli ($p$)

- **Concept:** A single trial with Success ($1$) or Failure ($0$).
- **Example:** A single switch is either ON or OFF.
- **Math:** $E[X] = p$, $Var(X) = p(1-p)$.

### 🔵 Binomial ($n, p$)

- **Concept:** Counting successes in $n$ fixed independent trials.
- **Example:** Number of "Heads" in 10 coin flips. Number of defective widgets in a batch of 50.
- **Math:** $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$.

### 🟡 Geometric ($p$)

- **Concept:** Counting _trials_ needed to get the **first** success.
- **Example:** Number of times you attempt to compile code until it runs without errors.
- **Math:** $P(X=k) = (1-p)^{k-1}p$.
- **Memoryless:** Past failures don't affect future probabilities.

### 🟣 Poisson ($\lambda$)

- **Concept:** Counting events in a fixed **interval** (time/space) given an average rate $\lambda$.
- **Example:** Number of cars passing a toll booth in 1 hour. Number of typos on a page of a book.
- **Math:** $P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}$.

---

## 3. Continuous Distributions (The "Measurers")

### 🟤 Uniform ($a, b$)

- **Concept:** "Flat" probability. Every interval of the same length is equally likely.
- **Example:** Waiting for a train that comes every 15 mins (wait time is $0$ to $15$).
- **Math:** $f(x) = \frac{1}{b-a}$.

### 🟠 Exponential ($\lambda$)

- **Concept:** Time _waiting_ until the next event (in a Poisson process).
- **Example:** Time until a radioactive particle decays. Time until a lightbulb burns out.
- **Math:** $f(x) = \lambda e^{-\lambda x}$ (for $x \ge 0$).
- **Calculus Note:** Integration by parts is often needed for $E[X]$.

### ⚪ Normal / Gaussian ($\mu, \sigma$)

- **Concept:** The Bell Curve. Nature's default distribution for sums of independent errors.
- **Example:** Physical measurement errors in a lab. Height of adult males.
- **Math:** Defined by Mean $\mu$ and Std Dev $\sigma$. (Standard Normal $Z$ has $\mu=0, \sigma=1$).

---

## 4. Joint Distributions (Multivariable Calculus Link)

### Key Definitions

- **Joint PDF:** $f(x,y)$ describes probability density at point $(x,y)$.
- **Volume = 1:** $\int \int f(x,y) dx dy = 1$.
- **Marginal PDF:** Integrating out one variable to "squash" the distribution onto an axis.
  - $f_X(x) = \int_{-\infty}^{\infty} f(x,y) dy$.
- **Independence:** $X, Y$ are independent if $f(x,y) = f_X(x) \cdot f_Y(y)$.
- **Covariance:** A measure of how two variables change together.
  - $Cov(X,Y) = E[XY] - E[X]E[Y]$.
  - If Independent, $Cov = 0$ (But $Cov=0$ doesn't always mean independent!).
