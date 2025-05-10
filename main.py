import json, argparse, os

import reports
from reports import reports_data, reports_extensions

files_path = 'files/'


def read_csv(filename: str) -> list:
    employees_data = []
    with open(filename, mode='r', newline='') as file:
        data = file.readlines()
        headers = data[0].strip().split(',')

        header_index = 0
        for index, header in enumerate(headers):
            if header.lower() in ['hourly_rate', 'rate', 'salary']:
                header_index = index
        headers[header_index] = 'hourly_rate'

        values = data[1:]
        for value in values:
            employee_data = dict(zip(headers, value.strip().split(',')))
            employees_data.append(employee_data)
    return employees_data


def print_report(report, report_name):
    from reports import reports_data
    print(f'{" ":>15}{"name":<16}', end='')
    for field in reports_data[report_name][0]:
        print(f'{f"{field}":<15}', end='')
    for field in reports_data[report_name][1]:
        print(f'{f"{field}":<15}', end='')
    print()
    for department, data in report.items():
        print(department)
        for employee in data['employees']:
            print('--------------', end=' ')
            print(f'{employee["name"]:<15}', end=' ')
            del employee["name"]
            for value in employee.values():
                print(f'{value:<15}', end='')
            print()
        if len(reports_data[report_name][1]) > 0:
            print(f'{report[department]["total_hours"]:>34} {"$":>27}{report[department]["total_payout"]} ')


def save_report(report, filename: str, report_format: str):
    converted_report = json.dumps(report, indent=2)
    directory = f'reports/{report_format}'
    if not os.path.exists(directory):
        os.makedirs(directory)
    new_file_name = filename.split('.')[0].split('\\')[-1] + f'.{report_format}'
    full_path = os.path.join(f'reports/{report_format}/', new_file_name)
    with open(full_path, 'w') as file:
        file.write(converted_report)


def generate_report(args, report_name, report_format):
    for file in args.files:
        if file.endswith('.csv'):
            try:
                data = read_csv(files_path + file)
                if data:
                    report = reports.get_report(data, report_name)
                    save_report(report, file, report_format)
                    print(f'Report for file "{file}": ')
                    print_report(report, report_name)
                    print('\n')
            except FileNotFoundError:
                print(f'Error: File "{file}" not found.')
        else:
            print(f'Incorrect file "{file}" entered. The file must have an extension ".csv"')


def main():
    parser = argparse.ArgumentParser(description='Generate reports from CSV files.')
    parser.add_argument('files', metavar='file', type=str, nargs='+', help='CSV files to process')
    parser.add_argument('--report', type=str, required=True, help='Type of report')
    parser.add_argument('--extension', type=str, required=True, help='File extension to generate')

    args = parser.parse_args()

    if args.report in reports_data.keys():
        if args.extension in reports_extensions:
            generate_report(args, args.report, args.extension)
        else:
            print('The report has not been generated! Enter the correct extension to save the report')
    else:
        print(f'Unknown report name: {args.report}. Please, enter correct report name')


if __name__ == '__main__':
    main()