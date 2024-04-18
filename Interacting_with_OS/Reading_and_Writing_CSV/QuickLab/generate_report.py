#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
  # Register a dialect use for file parsing
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

  employee_file = csv.DictReader(open(csv_file_location),
  dialect= 'empDialect')

  employee_list = []
  for employee in employee_file:
    employee_list.append(dict(employee))
  return employee_list


employee_list = read_employees('employees.csv')
print(employee_list)


# Function to process employee data
def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data["Department"])


  # Return the list of department as a dictionary with total number
  # of employees

  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)


  return department_data


dictionary = process_data(employee_list)
print(dictionary)


# generate report using the processed data
def write_report(dictionary, report_file):

  # open a file to write report
  with open(report_file, "w+") as file:
    for key, value in sorted(dictionary.items()):
      file.write(str(key) + ":" + str(value) + "\n")
    file.close()


write_report(dictionary, 'report.txt')