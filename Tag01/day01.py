def read_puzzle(file):
    elf = []
    with open(file) as f:
        for line in f.read().split("\n\n"):
            elf.append(line.split("\n"))
        return elf


def main():
    puzzle = read_puzzle("day01.txt")
    sum_calories = 0
    calorie_list = []

    for calorie in puzzle:
        for x in calorie:
            sum_calories = sum_calories + int(x)
        calorie_list.append(sum_calories)
        sum_calories = 0

    calorie_list.sort()

    print(calorie_list[-1])
    print(calorie_list[-1] + calorie_list[-2] + calorie_list[-3])

    return puzzle


if __name__ == '__main__':
    main()

