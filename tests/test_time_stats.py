from zvonok_test_assignment.time_stats import (calculate_work_hours,
                                               extract_employee_data,
                                               generate_output_view,
                                               time_stats,
                                               write_output_to_file)

PATH_INPUT_FILE = 'tests/fixtures/input.txt'
PATH_OUTPUT_FILE = 'tests/fixtures/output.txt'
DATA_LIST = [
    'Андрей 9', 'Василий 11', 'Роман 7', 'X Æ A-12 45', 'Иван Петров 3',
    'Настя 40', 'Андрей 6', 'Роман 11', 'Слава 40'
]
DATA_DICT = {
    'Андрей': {'hours': [9, 6], 'sum': 15},
    'Василий': {'hours': [11], 'sum': 11},
    'Роман': {'hours': [7, 11], 'sum': 18},
    'X Æ A-12': {'hours': [45], 'sum': 45},
    'Иван Петров': {'hours': [3], 'sum': 3},
    'Настя': {'hours': [40], 'sum': 40},
    'Слава': {'hours': [40], 'sum': 40}
}
DATA_STR = '''X Æ A-12: 45; sum: 45
Андрей: 9, 6; sum: 15
Василий: 11; sum: 11
Иван Петров: 3; sum: 3
Настя: 40; sum: 40
Роман: 7, 11; sum: 18
Слава: 40; sum: 40'''


def test_extract_employee_data() -> None:
    employee_data = extract_employee_data(PATH_INPUT_FILE)
    assert employee_data == DATA_LIST


def test_calculate_work_hours() -> None:
    hours_worked = calculate_work_hours(DATA_LIST)
    assert hours_worked == DATA_DICT


def test_generate_output_view() -> None:
    output_view = generate_output_view(DATA_DICT)
    assert output_view == DATA_STR


def test_write_output_to_file() -> None:
    with open(PATH_OUTPUT_FILE, 'r') as f:
        output = f.read()
    write_output_to_file('tests/fixtures/output_test.txt', DATA_STR)
    with open('tests/fixtures/output_test.txt', 'r') as f:
        output_test = f.read()
    assert output_test == output


def test_time_stats_with_output() -> None:
    with open(PATH_OUTPUT_FILE, 'r') as f:
        output = f.read()
    time_stats(PATH_INPUT_FILE, 'tests/fixtures/output_test2.txt')
    with open('tests/fixtures/output_test2.txt', 'r') as f:
        output_test = f.read()
    assert output_test == output


def test_time_stats_without_output() -> None:
    with open(PATH_OUTPUT_FILE, 'r') as f:
        output = f.read()
    output_test = time_stats(PATH_INPUT_FILE)
    assert output_test == output
