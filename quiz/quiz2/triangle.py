import math

def generate_right_triangles_with_perimeter(P):
    triangles = []
    for m in range(2, int(math.sqrt(P // 2)) + 1):
        for n in range(1 + m % 2, m, 2):  # opposite parity
            if math.gcd(m, n) != 1:
                continue
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            p = a + b + c
            if P % p == 0:
                k = P // p
                triangle = tuple(sorted((k*a, k*b, k*c)))
                triangles.append(triangle)
    return triangles

# Example
P = 13080
result = generate_right_triangles_with_perimeter(P)
for tri in result:
    print(tri)
