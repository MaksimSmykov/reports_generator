import pytest
import reports, main

@pytest.mark.parametrize(
    'file_name, report_name',
    [
        ('data3', 'payout'),
    ]
)
def test_get_report(file_name, report_name):
    assert type(reports.get_report(main.read_csv(f'files\\{file_name}.csv'), report_name)) == dict


@pytest.mark.parametrize(
    'hours_worked, hourly_rate, result',
    [
        (2, 5, 10),
        ('4', 15, 30),
    ]
)
def test_calculate_payout(hours_worked, hourly_rate, result):
    assert reports.calculate_payout(hours_worked, hourly_rate) == result
