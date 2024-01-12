import csv

file_path = 'aqms_data.csv'

def get_value(file_path, column_index):
    values = []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        for line_number, line in enumerate(csv_reader, start=1):
            try:
                values.append(float(line[column_index]))
            except (ValueError, IndexError):
                
                continue

    return values

def temperature():
    return(get_value(file_path, 0)[-1])

def pressure():
    return get_value(file_path, 1)[-1]

def humidity():
    return get_value(file_path, 2)[-1]

def gas():
    return get_value(file_path, 3)[-1]

def altitude():
    return get_value(file_path, 4)[-1]

def tvoc():
    return get_value(file_path, 5)[-1]

def eco2():
    return get_value(file_path, 6)[-1]

def raw_h2():
    return get_value(file_path, 7)[-1]

def raw_ethanol():
    return get_value(file_path, 8)[-1]
