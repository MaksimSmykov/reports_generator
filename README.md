# Reports_generator (Python 3.9)

> Reports_generator - generator of reports based on tables with employees data.

## Instructions

> To generate a report type the command in the console:
> 
> `python main.py data1.csv data2.csv data3.csv --report payout --extension json`
> 
>  where:
> - `main.py` - executable file name
> - `data1.csv data2.csv data3.csv` - names of source files with data (only .csv), separated by whitespace
> - `--report payout` - command to send the name of the report
> - `--extension json` - command to send the format for saving the report to a file

> Available reports:
> - `payout`

> Available formats to save reports:
> - `json`
> - `txt`

> File `main.py`:
> 
>  - `files_path` - source file path

> File `reports.py`:
> 
>  - `reports_data` - data about reports in the form of a dictionary:
>
> `dictionary key` - report name
> 
> `dictionary value` - tuple of tuples
> 
> where:
> 
> `tuple[0] - tuple of reports fields, which are in the source file`
> 
> `tuple[1] - tuple of additional reports fields (columns), which are calculated for an employee`
>
> `tuple[2] - tuple of additional reports fields (rows), which are calculated for a report field`
> 
> - `reports_extensions` - tuple of extensions to save generated report
