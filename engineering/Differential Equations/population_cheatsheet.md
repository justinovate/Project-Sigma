# 📘 Population Models in Differential Equations — Cheat Sheet

## 1. Basic Idea of Population Models

In population problems, we study **how a population changes over time**.

- Population usually depends on **time**
- We model this using **differential equations**
- The goal is often to **find the population at a certain time** or **describe its behavior**

We usually write:

\[
P(t) = \text{population at time } t
\]

---

## 2. Key Variables & Notation (Very Important)

| Symbol            | Meaning                                            |
| ----------------- | -------------------------------------------------- |
| \(P(t)\)          | Population at time \(t\)                           |
| \(\frac{dP}{dt}\) | Rate of change of population                       |
| \(t\)             | Time (years, months, days, etc.)                   |
| \(P_0\)           | Initial population (population at \(t = 0\))       |
| \(k\)             | Growth or decay constant                           |
| \(r\)             | Growth rate (often same role as \(k\))             |
| \(K\)             | Carrying capacity (maximum sustainable population) |

---

## 3. Exponential Growth Model (Unlimited Growth)

### 📌 When to Use This Model

Use this when:

- No limits on resources
- Population grows **proportionally to its size**
- Phrases like:
  - _“rate proportional to population”_
  - _“grows continuously”_
  - _“unlimited growth”_

---

### 🔹 Differential Equation

\[
\frac{dP}{dt} = kP
\]

---

### 🔹 Meaning

- The **rate of change** of population is proportional to the population itself

---

### 🔹 General Solution

\[
P(t) = P_0 e^{kt}
\]

---

### 🔹 Variable Explanation

| Variable  | Meaning                            |
| --------- | ---------------------------------- |
| \(P(t)\)  | Population at time \(t\)           |
| \(P_0\)   | Initial population                 |
| \(k > 0\) | Growth constant                    |
| \(t\)     | Time                               |
| \(e\)     | Euler’s number (\(\approx 2.718\)) |

---

### 🔹 Interpretation of \(k\)

| Value of \(k\) | Meaning           |
| -------------- | ----------------- | --- | ------------- |
| \(k > 0\)      | Population grows  |
| \(k < 0\)      | Population decays |
| Larger \(      | k                 | \)  | Faster change |

---

### 🧠 Common Word Problem Steps

1. Identify **initial population** \(P_0\)
2. Write the DE: \(\frac{dP}{dt} = kP\)
3. Use given information to find \(k\)
4. Plug into \(P(t) = P_0 e^{kt}\)
5. Evaluate at required time

---

## 4. Exponential Decay Model

### 📌 When to Use

- Population **decreases**
- Phrases like:
  - _“declines at a rate proportional to population”_
  - _“death rate exceeds birth rate”_

---

### 🔹 Formula

\[
P(t) = P_0 e^{kt}, \quad k < 0
\]

Same formula as growth — **only the sign of \(k\) changes**.

---

## 5. Logistic Growth Model (Limited Growth)

### 📌 When to Use This Model

Use this when:

- Resources are limited
- Population levels off over time
- Words like:
  - _“carrying capacity”_
  - _“maximum sustainable population”_
  - _“slows as population increases”_

---

### 🔹 Differential Equation

\[
\frac{dP}{dt} = kP\left(1 - \frac{P}{K}\right)
\]

---

### 🔹 Meaning

- Population grows fast when small
- Growth slows as \(P \to K\)
- Population **never exceeds \(K\)**

---

### 🔹 Logistic Solution Formula

\[
P(t) = \frac{K}{1 + Ae^{-kt}}
\]

where

\[
A = \frac{K - P_0}{P_0}
\]

---

### 🔹 Variable Explanation

| Variable | Meaning                         |
| -------- | ------------------------------- |
| \(K\)    | Carrying capacity               |
| \(P_0\)  | Initial population              |
| \(k\)    | Growth constant                 |
| \(A\)    | Constant from initial condition |

---

### 🧠 Key Behavior

| Population Size | Behavior                |
| --------------- | ----------------------- |
| \(P \ll K\)     | Near exponential growth |
| \(P = K/2\)     | Maximum growth rate     |
| \(P \to K\)     | Growth slows to zero    |

---

## 6. Population with Constant Immigration/Harvesting

### 📌 When to Use

- Population gains or loses **a fixed number** per time
- Words like:
  - _“500 people immigrate per year”_
  - _“harvested at a constant rate”_

---

### 🔹 Differential Equation

\[
\frac{dP}{dt} = kP + C
\]

Where:

- \(C > 0\): immigration
- \(C < 0\): harvesting

---

### 🔹 General Solution

\[
P(t) = Ce^{-kt} + \frac{C}{k}
\quad \text{(after solving)}
\]

(Solution usually found using **integrating factor**)

---

## 7. How to Solve Population Word Problems (Checklist)

### ✅ Step-by-Step Strategy

1. **Define the variable**

   - Let \(P(t)\) = population at time \(t\)

2. **Identify the model**

   - Proportional → Exponential
   - Limited growth → Logistic
   - Constant addition/removal → Immigration model

3. **Write the DE**

4. **Use initial condition**

   - Given as “initially” or “at \(t=0\)”

5. **Solve for constants**

6. **Answer the question**
   - Population at a given time
   - Time to reach a population
   - Long-term behavior

---

## 8. Common Mistakes to Avoid 🚫

- ❌ Forgetting to define variables
- ❌ Mixing time units (years vs months)
- ❌ Using exponential model when carrying capacity is mentioned
- ❌ Forgetting initial condition
- ❌ Sign error in \(k\)

---

## 9. Quick Comparison Table

| Model              | Formula                        | When to Use             |
| ------------------ | ------------------------------ | ----------------------- |
| Exponential Growth | \(P = P_0 e^{kt}\)             | Unlimited growth        |
| Exponential Decay  | \(P = P_0 e^{kt}\)             | Decline                 |
| Logistic           | \(P = \frac{K}{1 + Ae^{-kt}}\) | Limited resources       |
| Immigration        | \(\frac{dP}{dt} = kP + C\)     | Constant inflow/outflow |

---
