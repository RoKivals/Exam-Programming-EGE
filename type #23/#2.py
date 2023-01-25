def Prog(current_num, goal):
    if current_num > goal:
        return 0
    if current_num == goal:
        return 1
    return Prog(current_num + 1, goal) + Prog(current_num + 2, goal) + Prog(current_num + 4, goal)


def main():
    # Путь от 1 до 15, который включает в себя 8.
    print(Prog(1, 8) * Prog(8, 15))


if __name__ == '__main__':
    main()
