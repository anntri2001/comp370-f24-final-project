import os
import csv
import json
import argparse
from newscover.thenewsapi import thenewsapi
from newscover.json_to_tsv import convert_from_json_to_tsv

published_on_dates = [
    '2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04', '2024-06-05', 
    # '2024-06-06', '2024-06-07', '2024-06-08', '2024-06-09', '2024-06-10', 
    # '2024-06-11', '2024-06-12', '2024-06-13', '2024-06-14', '2024-06-15', 
    # '2024-06-16', '2024-06-17', '2024-06-18', '2024-06-19', '2024-06-20', 
    # '2024-06-21', '2024-06-22', '2024-06-23', '2024-06-24', '2024-06-25', 
    # '2024-06-26', '2024-06-27', '2024-06-28', '2024-06-29', '2024-06-30', 
]

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--api-key", required=True)
    parser.add_argument("-i", "--input", help="input json with search parameters", required=True)
    parser.add_argument("-o", "--output", help="output fname", required=True)
    parser.add_argument("-t", "--tsv", help="tsv fname", default=0)
    args = parser.parse_args()
    return args

def read_json(fname):
    json_fname = os.path.join(os.path.dirname(__file__), fname)
    with open(json_fname, "r") as f:
        contents = json.load(f)
    return contents

def convert_to_tsv(json_fname, tsv_fname, json_objects):
    json_fname = (os.path.join(os.path.dirname(__file__), json_fname)) 
    tsv_fname = (os.path.join(os.path.dirname(__file__), tsv_fname))
    convert_from_json_to_tsv(json_fname, tsv_fname)

def collector():
    args = init_parser()
    contents = read_json(args.input)
    oname = (os.path.join(os.path.dirname(__file__), args.output))
    results = []
    with open(oname, "w") as f:
        for keywords in list(contents.values()):
            for d in published_on_dates:
                response = json.loads(thenewsapi(args.api_key, keywords, d))
                results = results + response
        json.dump(results, f, indent=4)
    
    if args.tsv: convert_to_tsv(args.output, args.tsv, results[0])

if __name__ == "__main__":
    collector()