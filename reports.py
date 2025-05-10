from typing import Union

reports_data = {
    'payout': (('hours_worked', 'hourly_rate', ), ('payout',), ('total_hours', 'total_payout')),
    'avg_rate': (('hourly_rate',), (), ('average_rate',)),
}

reports_extensions = ('json', 'txt')


def calculate_payout(hours_worked: Union[int, float], hourly_rate: Union[int, float]) -> Union[int, float]:
    if ((isinstance(hours_worked, int) or isinstance(hours_worked, float)) and
            (isinstance(hourly_rate, int) or isinstance(hourly_rate, float))):
        return hours_worked * hourly_rate
    else:
        raise TypeError('Incorrect input data format')


def get_report(employees, report_name):
    global reports_data
    report = {}

    for employee in employees:
        report_fields = {}
        department = employee['department']
        name = employee['name']
        report_fields['name'] = name

        for field in reports_data[report_name][0]:
            if employee[f'{field}'].isdigit():
                value = int(employee[f'{field}'])
            else:
                value = employee[f'{field}']
            report_fields[field] = value

        if department not in report:
            report[department] = {
                'employees': [],
            }
            # Adding additional rows for the overall calculation by department
            if len(reports_data[report_name][2]) > 0:
                for field in reports_data[report_name][2]:
                    report[department][f'{field}'] = 0

        if len(reports_data[report_name][1]) > 0:
            hours = int(employee['hours_worked'])
            rate = int(employee['hourly_rate'])
            payout = calculate_payout(hours, rate)
            report[department]['total_hours'] += hours
            report[department]['total_payout'] += payout
            report_fields['payout'] = payout

        report[department]['employees'].append(report_fields)
    return report
