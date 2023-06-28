import os


def extract_employee_data(path: str) -> list[str]:
    absolute_path = os.path.abspath(path)
    employee_data = []
    with open(absolute_path, 'r') as file:
        for line in file:
            employee_data.append(line.strip())

    return employee_data


def calculate_work_hours(data: list[str]) -> dict:
    hours_worked = {}
    for row in data:
        separator_index = -(row[::-1].index(' '))
        name = row[:separator_index].strip()
        hour_count = int(row[separator_index:].strip())

        if name not in hours_worked:
            hours_worked[name] = {
                'hours': [hour_count],
                'sum': hour_count
            }
        else:
            hours_worked[name]['hours'].append(hour_count)
            hours_worked[name]['sum'] += hour_count

    return hours_worked


def generate_output_view(data: dict) -> str:
    output_view = ''
    for emp in sorted(data.keys()):
        hours = ', '.join([str(h) for h in data[emp]['hours']])
        hour_sum = str(data[emp]['sum'])
        output_view += f'{emp}: {hours}; sum: {hour_sum}\n'

    return output_view.strip()


def write_output_to_file(path: str, data: str) -> str:
    absolute_path = os.path.abspath(path)
    with open(absolute_path, 'w') as file:
        file.write(data)
    return absolute_path


def time_stats(path_input: str, path_output: str = None):
    employee_data = extract_employee_data(path_input)
    hours_worked = calculate_work_hours(employee_data)
    output_view = generate_output_view(hours_worked)
    if path_output:
        return write_output_to_file(path_output, output_view)
    return output_view
