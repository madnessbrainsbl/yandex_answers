import sys


def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr]);
    ptr += 1

    Q = list(map(int, input[ptr:ptr + N]))
    ptr += N

    C = list(map(int, input[ptr:ptr + N]))
    ptr += N

    A, B = map(int, input[ptr:ptr + 2])
    ptr += 2

    D = []
    if A == B:
        D = [A] * N
    else:
        for Ci in C:
            Di = A + (Ci * (B - A)) / 255
            D.append(Di)

    dot_product = 0
    for Qi, Di in zip(Q, D):
        dot_product += Qi * Di

    print(int(round(dot_product)))


if __name__ == "__main__":
    main()
