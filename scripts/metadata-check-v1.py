import os
import re

def list_files(dir):
    ignored_dirs = { ".sentinel", "common-functions", "test"}
    all_files = [x for x in os.listdir(dir) if x not in ignored_dirs]
    all_sentinel_files = []
    for files in all_files:
        if files.endswith('.sentinel'):
            all_sentinel_files.append(files)
            # print(files,end="\n")
            file_path = dir + "/" + files
            # ------------------------------------
            # Call read_metadata function to parse the file and write a dictonery of metatda
            # ------------------------------------
           
            # -----------------------------------
            # Regular expression to match the naming convention
            # -----------------------------------
            pattern = '^GCP-TFSENTINEL-[A-Za-z]{3,10}-[0-9]{3,3}-[0-9]{3,3}.sentinel'
            result = re.match(pattern, files)
            if result:
                print("Nameing convention followed.")
            else:
                print(files,"........... Naming convention Not Followed.")
                exit(1)
            
            read_metadata(file_path)

    return (all_sentinel_files)

def read_metadata(path):
    print("path is:", path)
    print("\n")
    print("---------------------------------------------")
    print("\n")
    metadata_list = []
    version_count = 0
    category_count = 0
    priority_count = 0
    customcacref_count = 0
    createdby_count = 0
    policyname_count = 0
    policydesc_count = 0
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
                version_count = version_count + 1
     
            if '"category":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                category_count = category_count + 1

            if '"priority":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                priority_count = priority_count + 1

            if '"customComplianceCacRef":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                customcacref_count = customcacref_count + 1
  
            if '"createdBy":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                createdby_count = createdby_count + 1
        
            if '"policyName":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                policyname_count = policyname_count + 1
            
            if '"policyDescription":' in line:
                trimmed_line = line.lstrip()
                seperator = ','
                stripped = trimmed_line.split(seperator,1)[0]
                strip_quotes = stripped.replace('"', '')
                val_val = strip_quotes.split(':')[1]
                final_val = val_val.strip()
                metadata_list.append(final_val)
                policydesc_count = policyid_count + 1
                #print(metadata_list)
        
        if version_count == 0:
            print("version missing or version metadata is wrong in:", path)
            exit(1)
        if category_count == 0:
            print("category missing or metadata issue in:", path)
            exit(1)
        if priority_count == 0:
            print("Priority missing or metadata issue in:", path)
            exit(1)
        if customcacref_count == 0:
            print("CustomComplianceCacRef missing or metadata issue in:", path)
            exit(1)
        if createdby_count == 0:
            print("CreatedBy missing or metadata issue in:", path)
            exit(1)
        if policyname_count == 0:
            print("PolicyName missing or metadata issue in:", path)
            exit(1)
        if policydesc_count == 0:
            print("PolicyDescription is missing or metadata issue in:", path)
            exit(1)
                     
    return
   


policies_names = []
policies_names = list_files("policies")
# print("-------------------------------------------------------")
# print("Total No of Sentinel Policies are:", len(policies_names))
# print("-------------------------------------------------------")
# print(policies_names, end="\n")