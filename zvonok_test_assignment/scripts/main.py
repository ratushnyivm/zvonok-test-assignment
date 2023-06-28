from zvonok_test_assignment.cli import parse_input
from zvonok_test_assignment.time_stats import time_stats


def main():
    args = parse_input()
    print(time_stats(args.path_input, args.output))


if __name__ == '__main__':
    main()
