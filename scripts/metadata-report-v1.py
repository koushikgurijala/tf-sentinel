import os
import csv
from datetime import datetime

def list_files(dir):
    ignored_dirs = { ".sentinel", "common-functions", "test"}
    all_files = [x for x in os.listdir(dir) if x not in ignored_dirs]
    all_sentinel_files = []
    for files in all_files:
        if files.endswith('.sentinel'):
            all_sentinel_files.append(files)
            print(files)
            print("\n")
            file_path = dir + "/" + files
            # ------------------------------------
            # Call read_metadata function to parse the file and write a dictonery of metatda
            # ------------------------------------
            read_metadata(file_path)
    return (all_sentinel_files)

def read_metadata(path):
    print("path is:", path)
    print("\n")
    print("---------------------------------------------")
    print("\n")
    metadata_dict = {}
    metadata_list = []
    with open(path,'r') as reader:
        count = 0
        for line in reader:
            if '"version":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                # metadata_dict.update({'version': final_val})
                # print(metadata_dict)
            if '"category":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                # print(metadata_dict)
            if '"priority":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                # print(metadata_dict)
            if '"customComplianceCacRef":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                # print(metadata_dict)
            if '"createdBy":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                # print(metadata_dict)
            if '"policyDescription":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                #print(metadata_dict)
            if '"policyName":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                #print(metadata_dict)
                write_data_to_csv(metadata_list)
    return
   


def write_data_to_csv(result_list):
    #csv_columns = ['version', 'category', 'priority', 'customComplianceCacRef', 'createdBy', 'policyName', 'policyId]
    #csv_file = "TF-Sentinel-Policies-Summary-" + datetime.now().strftime('%m-%d-%Y_%H-%M') + ".csv"
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
            #writer.writerow(csv_columns)
            writer.writerow(result_list)
            print(result_list)
            
    except IOError:
        print("I/O Error")
    return

def write_header_to_csv():
    csv_columns = ['version', 'category', 'priority', 'customComplianceCacRef', 'createdBy', 'policyDescription', 'policyName']
    global csv_file
    csv_file = "TF-Sentinel-Policies-Summary-" + datetime.now().strftime('%m-%d-%Y_%H-%M') + ".csv"
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(csv_columns)
 
    except IOError:
        print("I/O Error")
    return


policies_names = []
write_header_to_csv()
policies_names = list_files("policies")
# print("-------------------------------------------------------")
# print("Total No of Sentinel Policies are:", len(policies_names))
# print("-------------------------------------------------------")
#print(policies_names, end="\n")