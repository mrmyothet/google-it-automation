#!/usr/bin/env python3

import csv


def read_employees(csv_file_location):
    csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect="empDialect")

    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list


def process_data(employee_list):
    department_list = []

    for employee_data in employee_list:
        department_list.append(employee_data["department"])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ":" + str(dictionary[k]) + "\n")
        f.close()


csv_file_location = "/home/myothet/repos/google-it-automation/interact-with-os/2_Managing_Files/by_department.csv"
employee_list = read_employees(csv_file_location)
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)

write_report(
    dictionary,
    "/home/myothet/repos/google-it-automation/interact-with-os/2_Managing_Files/employee_report.txt",
)
