import os
import csv

cwd = os.getcwd()
print(cwd)
year = "2021"c
table_id = "A1-1"
if len(table_id) < 5:
    table_id += " "

# Location of CRA files
file_location_cra_raw_files = os.path.join(cwd, "Fall_2023_Data", "Raw_Data_CRA", year)
print(file_location_cra_raw_files)

# From years 2011 until 2015
# file_name_cra = "exp_aggr.dat"
# From years 2016 until 2021
file_name_cra = "exp_aggr_" + table_id.strip(" ") + ".dat"

# Output folder where mdi data will be stored.
output_location = os.path.join(cwd, "Fall_2023_Data", "Data_extracted_csv", year)
if not os.path.exists(output_location):
    os.makedirs(output_location)

print(output_location)

# Finding out if I can get the correct CRA file
data_file_path = os.path.join(file_location_cra_raw_files, file_name_cra)
print(data_file_path)

# Field specification is a custom-made csv based on file specs with each dat file
file_field_specification = "CRA_Flat_Agg_Specs.csv"
file_field_specification_path = os.path.join(cwd, file_field_specification)
print(file_field_specification_path)

# Name of the file that is finally extracted
file_name_after_iteration = year + "_aggr_" + table_id

# This is obtained from the file specs
field_specification_list = []


class FieldSpecification:
    def __init__(self, name, start, end, length):
        self.name = name
        self.start_position = start
        self.end_position = end
        self.length = length

    def get_value_from_line(self, line):
        value = line[self.start_position - 1:self.end_position]
        return value


def read_field_specification_from_csv(filepath):
    with open(filepath, mode='r') as csv_file:
        specification_file_reader = csv.reader(csv_file)
        next(specification_file_reader)

        for row in specification_file_reader:
            new_field_specification = FieldSpecification(row[0], int(row[1].strip()), int(row[2].strip()),
                                                         int(row[3].strip()))
            if new_field_specification.name.lower() != "filler":
                field_specification_list.append(new_field_specification)


def store_dat_file_data_to_list(filepath):
    dat_file = open(filepath, "r")
    all_records_list = []

    for line in dat_file:
        current_record_list = []
        if table_id == line[:5]:
            for field_spec in field_specification_list:
                current_record_list.append(field_spec.get_value_from_line(line))
            all_records_list.append(current_record_list)

    dat_file.close()

    return all_records_list


def write_records_into_csv(records):
    csv_file_path = os.path.join(output_location, file_name_after_iteration + ".csv")

    with open(csv_file_path, 'w', newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        header_list = []
        for field_spec in field_specification_list:
            header_list.append(field_spec.name)

        csv_writer.writerow(header_list)
        csv_writer.writerows(records)


read_field_specification_from_csv(file_field_specification_path)
records_list = store_dat_file_data_to_list(data_file_path)
write_records_into_csv(records_list)
