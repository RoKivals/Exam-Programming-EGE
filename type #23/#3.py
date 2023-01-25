def Prog(curr_pos, goal, blocked):
    if curr_pos > goal or curr_pos == blocked: return 0
    if curr_pos == goal: return 1

    return Prog(curr_pos + 1, goal, blocked) + Prog(curr_pos + 2, goal, blocked)


def main():
    print(Prog(3, 9, 15) * Prog(9, 20, 15))


if __name__ == '__main__':
    main()
