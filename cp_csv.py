import csv

def parse(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        header = csv_reader.fieldnames
        print(f'Header: {header}')
        return csv_reader
        