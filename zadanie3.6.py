A = [5, 2, 4, 1]
n = 0
for j in range(n - 1):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
print(A)