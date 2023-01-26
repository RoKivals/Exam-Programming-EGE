import sys


def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)

# Линейное решение задачи
# def F(n):
#     cnt = 1
#     while n:
#         if n == 1:
#             return cnt
#         elif n > 1:
#             cnt *= n
#             n -= 1


def main():
    # Переопределение глубины рекурсии
    sys.setrecursionlimit(2030)
    print(F(2023) / F(2020))


if __name__ == "__main__":

    main()
