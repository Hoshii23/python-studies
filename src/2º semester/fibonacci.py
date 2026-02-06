n = 50  # Number of terms
a, b = 0, 1
sequence = []

for _ in range(n):
    sequence.append(a)
    a, b = b, a + b

print(f"Fibonacci sequence up to {n} terms: {sequence}")