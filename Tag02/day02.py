def read_puzzle(file):
    with open(file) as f:
        return [line.split() for line in f.read().split("\n")]


def main():
    puzzle = read_puzzle("day02.txt")

    score_part1 = 0
    score_part2 = 0
    rock, paper, scissor = 1, 2, 3
    win = 6
    draw = 3

    for a, b in puzzle:
        a = ord(a) - 64
        b = ord(b) - 87
        score_part1 += rock if b == rock else paper if b == paper else scissor
        score_part2 += draw if b == paper else win if b == scissor else 0

        if a == b:
            score_part1 += draw
        elif a == rock and b == paper or a == paper and b == scissor or a == scissor and b == rock:
            score_part1 += win

        if b == rock:
            if a == rock:
                score_part2 += scissor
            elif a == paper:
                score_part2 += rock
            else:
                score_part2 += paper
        if b == paper:
            if a == rock:
                score_part2 += rock
            elif a == paper:
                score_part2 += paper
            else:
                score_part2 += scissor
        if b == scissor:
            if a == rock:
                score_part2 += paper
            elif a == paper:
                score_part2 += scissor
            else:
                score_part2 += rock

    print(score_part1, score_part2)
    return puzzle


if __name__ == '__main__':
    main()
