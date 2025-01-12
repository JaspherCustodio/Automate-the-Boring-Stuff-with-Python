# Diamond shape pattern
n = 5
# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
print()

# Right-Aligned Triangle
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
print()

# Number Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(str(x) for x in range(1, i + 1)))
print()

# Hollow Diamond
n = 5
# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" + " " * (2 * (i - 1) - 1) + ("*" if i > 1 else ""))
# Lower half
for i in range(n - 1, 0 , -1):
    print(" " * (n - i) + "*" + " " * (2 * (i - 1) - 1) + ("*" if i > 1 else ""))
print()

# Hourglass pattern
n = 5
# Upper half
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Lower half
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
print()

# Alphabet Diamond
n = 5
alpha = 65 # ASCII FOR A

# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(chr(alpha + j) for j in range(i)))
# Lower half
for i in range(n - 1, 0 , -1):
    print(" " * (n - i) + " ".join(chr(alpha + j) for j in range(i)))
