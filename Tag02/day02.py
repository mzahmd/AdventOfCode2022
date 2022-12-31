def read_puzzle(file):
    with open(file) as f:
        for line in f:
            print(line)
        return line


def main():
    puzzle = read_puzzle("day02.txt")

    return puzzle


if __name__ == '__main__':
    main()

