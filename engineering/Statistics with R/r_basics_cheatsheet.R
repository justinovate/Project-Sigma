# ================================
# R BASICS CHEATSHEET
# ================================

# ----------------
# 1. Variables
# ----------------
x <- 10
y <- 3.5
name <- "Alice"
is_valid <- TRUE

# ----------------
# 2. Basic Data Types
# ----------------
# numeric, integer, character, logical
class(x)
class(name)

# ----------------
# 3. Vectors
# ----------------
v <- c(1, 2, 3, 4, 5)

v[1]  # indexing (1-based)
length(v)
sum(v)
mean(v)

# ----------------
# 4. Sequences
# ----------------
seq(1, 10, by = 2)
rep(1, times = 5)

# ----------------
# 5. Matrices
# ----------------
m <- matrix(1:6, nrow = 2, ncol = 3)

m[1,2]  # row, column
t(m)    # transpose
dim(m)

# ----------------
# 6. Lists
# ----------------
lst <- list(
  numbers = v,
  text = "hello",
  flag = TRUE
)

lst$numbers

# ----------------
# 7. Data Frames
# ----------------
df <- data.frame(
  id = c(1, 2, 3),
  score = c(85, 90, 78),
  passed = c(TRUE, TRUE, FALSE)
)

head(df)
str(df)

df$score
df[df$score > 80, ]

# ----------------
# 8. Control Flow
# ----------------
if (x > 5) {
  print("x is greater than 5")
} else {
  print("x is 5 or less")
}

for (i in v) {
  print(i)
}

# ----------------
# 9. Functions
# ----------------
add_numbers <- function(a, b) {
  return(a + b)
}

add_numbers(2, 3)

# ----------------
# 10. Apply Functions
# ----------------
apply(m, 1, sum)  # rows
apply(m, 2, sum)  # columns

lapply(lst, class)

# ----------------
# 11. Basic Plotting
# ----------------
plot(c, type = "b", col = "blue")
hist(v)

# ----------------
# 12. Reading & Writing Data
# ----------------
# df <- read.csv("data.csv")
# write.csv(df, "output.csv", row.names = FALSE)
