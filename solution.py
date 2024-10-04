import sys


def main():
    input_data = sys.stdin.read()
    lines = input_data.strip().splitlines()
    N = int(lines[0])
    results = process_test_cases(lines, 1, N)
    for result in results:
        print(result)


def process_test_cases(lines, index, N):
    if N == 0:
        return []
    else:
        X = int(lines[index])
        Yn_line = lines[index + 1]
        Yn = Yn_line.strip().split()
        Yn_int = list(map(int, Yn))
        positive_Yn = list(filter(lambda x: x >= 0, Yn_int))
        sum_of_squares = sum(map(lambda x: x * x, positive_Yn))
        return [sum_of_squares] + process_test_cases(lines, index + 2, N - 1)


if __name__ == '__main__':
    main()
