#!/usr/bin/python3
import csv
import sys
import re

# Read model name table
codename_reader = csv.DictReader(open("./table.csv"))
remove_useless = re.compile("[|#].*")
model_dict = {}
for i in codename_reader:
    codename = i[" codename"][1:]
    model = re.sub(remove_useless, "", i[" Model"])[1:]
    model_dict[codename] = model

# Parse input and add model name
input_reader = csv.DictReader(sys.stdin)
field_names = list(input_reader.fieldnames)
field_names.insert(-1, "model")

def wrapper(gen):
    """ Iterator wrapper to ignore malformed CSV exceptions """
    while True:
        try:
            yield next(gen)
        except StopIteration:
            raise
        except Exception as e:
            print(e, file=sys.stderr)
            pass

writer = csv.DictWriter(sys.stdout, field_names)
writer.writeheader()
for i in wrapper(input_reader):
    i["model"] = model_dict.get(i["name"], "Unknown")
    try:
        writer.writerow(i)
    except:
        pass
