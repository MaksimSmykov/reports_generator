import pytest, os
import reports, main


@pytest.mark.parametrize(
    'file_name, result',
    [
        ('files/data1.csv', list),
    ]
)
def test_read_csv(file_name, result):
    assert type(main.read_csv(file_name)) == result


@pytest.mark.parametrize(
    'file_name, report_name, result',
    [
        ('files/data1.csv', 'payout', dict),
    ]
)
def test_print_report(file_name, report_name, result):
    data = main.read_csv(file_name)
    report = reports.get_report(data, report_name)
    assert type(report) == result


@pytest.mark.parametrize(
    'file_name, report_name, final_path',
    [
        ('data1.csv', 'payout', 'reports/json/data1.json'),
    ]
)
def test_save_report(file_name, report_name, final_path):
    data = main.read_csv(main.files_path + file_name)
    report = reports.get_report(data, report_name)
    main.save_report(report, file_name, 'json')
    assert os.path.exists(final_path) == True


@pytest.mark.parametrize(
    'file_name, report_name, final_path',
    [
        ('data1.csv', 'payout', 'reports/txt/data1.txt'),
    ]
)
def test_generate_report(file_name, report_name, final_path):
    data = main.read_csv(main.files_path + file_name)
    report = reports.get_report(data, report_name)
    main.save_report(report, file_name, 'txt')
    assert os.path.exists(final_path) == True


@pytest.mark.parametrize(
    'file_name, report_name, final_path',
    [
        ('data3.csv', 'payout', 'reports/txt/data3.txt'),
    ]
)
def test_main(file_name, report_name, final_path):
    data = main.read_csv(main.files_path + file_name)
    report = reports.get_report(data, report_name)
    main.save_report(report, file_name, 'txt')
    assert os.path.exists(final_path) == True