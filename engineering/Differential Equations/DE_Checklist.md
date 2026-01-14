# 🚀 Calculus → Differential Equations Master Checklist

**Status:** In Progress
**Priority:** High (Due in 3 Days)

---

## 🧮 PART A: Calculus Foundations (The Toolbelt)

_You cannot solve DEs if you cannot do these specific derivatives and integrals._

### 1️⃣ Derivatives (Non-Negotiable)

- [x] **Power Rule:** $\frac{d}{dx}x^n = nx^{n-1}$
- [x] **Chain Rule:** $f(g(x))' = f'(g(x))g'(x)$ _(Most common error source)_
- [x] **Product Rule:** $(uv)' = u'v + uv'$ _(Required for Linear DE proofs)_
- [x] **Implicit Differentiation:** For when you can't isolate $y$.
- [ ] **Essential Functions:**
  - [ ] $e^x, a^x$
  - [ ] $\ln(x)$
  - [ ] $\sin(x), \cos(x)$

### 2️⃣ Integrals (The Solvers)

- [x] **Basic Antiderivatives:** Power rule in reverse.
- [ ] **The Constant ($+C$):** Never forget this!
- [x] **U-Substitution:** The #1 technique used in DEs.
- [x] **Integration by Parts (LIATE):** $\int u dv = uv - \int v du$
- [ ] **Partial Fraction Decomposition:** Essential for Logistic Growth ($\int \frac{1}{y(1-y)} dy$).
- [ ] **Logarithmic Integrals:** Remember $\int \frac{1}{y} dy = \ln|y|$.

### 3️⃣ Algebra Skills (The Setup)

- [x] **Factoring:** separating $dy/dx = xy + x$ into $x(y+1)$.
- [x] **Laws of Exponents:** $e^{a+b} = e^a \cdot e^b$.
- [x] **Log Rules:** $e^{\ln x} = x$ and $\ln(ab) = \ln a + \ln b$.
- [ ] **Handling Constants:** Understanding that $e^{C}$ is just a new constant $C_1$.

---

## 📘 PART B: Differential Equations Syllabus

### ✅ CO1OL1 — Introduction to DEs

- [x] **Classify:** Order, Linearity, ODE vs PDE.
- [x] **Verification:** Check if a function is a solution by plugging it in.
- [x] **Initial Value Problems (IVP):** Solve for $C$ using $y(x_0)=y_0$.

### ✅ CO1OL2 — Direction Fields & Autonomous Eqs

- [ ] **Direction Fields:** Sketch slopes without solving.
- [ ] **Equilibrium Solutions:** Set $y' = 0$ and solve for $y$.
- [ ] **Stability:** Classify as **Stable** (Sink), **Unstable** (Source), or **Semi-stable** (Node).
- [ ] **Phase Lines:** Draw vertical stability diagrams.

### 🔥 CO1OL3 — Linear & Separable Equations (TOP PRIORITY)

**Type 1: Separable Equations ($y' = g(x)h(y)$)**

- [ ] **Separate:** Group $y$ terms with $dy$, $x$ terms with $dx$.
- [ ] **Integrate:** Perform integration on both sides.
- [ ] **Solve:** Isolate $y(x)$ explicitly if possible.
- [ ] **Check Singularities:** Did you divide by zero (e.g., $y=0$)?

**Type 2: First-Order Linear Equations ($y' + P(x)y = Q(x)$)**

- [ ] **Standard Form:** Ensure coefficient of $y'$ is 1.
- [ ] **Integrating Factor:** Calculate $\mu(x) = e^{\int P(x) dx}$.
- [ ] **Multiply:** Apply $\mu(x)$ to the whole equation.
- [ ] **Collapse:** Recognize LHS as $\frac{d}{dx}[\mu(x)y]$.
- [ ] **Solve:** Integrate both sides and divide by $\mu(x)$.

### ✅ CO1OL4 — Basic Applications

- [ ] **Growth/Decay:** $y' = ky$ (Population, Radioactive Decay).
- [ ] **Newton’s Law of Cooling:** $T' = k(T - T_{env})$.
- [ ] **Mixing Problems:** $\frac{dy}{dt} = \text{Rate}_{in} - \text{Rate}_{out}$.
