import argparse


def parse_input():
    parser = argparse.ArgumentParser(
        description='Shows the statistics of the time worked by the employee.'
    )
    parser.add_argument(
        'path_input',
        type=str
    )
    parser.add_argument(
        '-o', '--output',
        help='set path for writing results to file (default: "not specified")',
        default=None
    )
    args = parser.parse_args()

    return args
