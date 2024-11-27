import os
import csv
import json
import argparse

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input json file", required=True)
    parser.add_argument("-o", "--output", help="output tsv name", required=True)
    args = parser.parse_args()
    return args

def convert_from_json_to_tsv(json_fname, tsv_fname):
    with open(json_fname, "r") as f:
        contents = json.load(f)

    with open(tsv_fname, mode='w', newline='', encoding='utf-8') as f:
        headers = list(contents[0].keys())
        writer = csv.DictWriter(f, fieldnames=headers, delimiter='\t')
        writer.writeheader()
        for row in contents:
            writer.writerow(row)

def json_to_tsv():
    args = init_parser()
    json_fname = os.path.join(os.path.dirname(__file__), args.input)
    tsv_fname = os.path.join(os.path.dirname(__file__), args.output)
    convert(json_fname, tsv_fname)

if __name__ == '__main__':
    # json_to_tsv()
    # json_dir_path = "/home/atrinh/final-project/comp370-f24-final-project/newscover/data/jsons"
    # convert_to_one_file(json_dir_path, "all_titles.tsv")
    convert_from_json_to_tsv('test.json', 'test.tsv')
