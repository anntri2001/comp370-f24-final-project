import os
import csv
import json
import argparse
from newscover.thenewsapi import thenewsapi
from newscover.json_to_tsv import convert_from_json_to_tsv

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--api-key", required=True)
    parser.add_argument("-i", "--input", help="input json with search parameters", required=True)
    parser.add_argument("-s", "--start-date", default='2024-06-01')
    parser.add_argument("-e", "--end-date", default='2024-06-30')
    parser.add_argument("-o", "--output", help="output directory", required=True)
    parser.add_argument("-t", "--tsv", default=0)
    args = parser.parse_args()
    return args

def read_json(fname):
    json_fname = os.path.join(os.path.dirname(__file__), fname)
    with open(json_fname, "r") as f:
        contents = json.load(f)
    return contents

def convert_to_tsv(args, json_objects):
    for obj in json_objects:
        json_fname = os.path.join((os.path.join(os.path.dirname(__file__), os.path.join(args.output, "jsons"))), obj + ".json")
        tsv_fname = os.path.join((os.path.join(os.path.dirname(__file__), args.output)), obj + ".tsv")

        convert_from_json_to_tsv(json_fname, tsv_fname)

def collector():
    args = init_parser()
    contents = read_json(args.input)
    for i in contents:
        dir = (os.path.join(os.path.dirname(__file__), args.output))
        odir = os.path.join(dir, "jsons")
        if not os.path.isdir(dir): os.mkdir(dir)
        if not os.path.isdir(odir): os.mkdir(odir)

        oname = os.path.join(odir, i + ".json")
        with open(oname, "w") as f:
            for t in contents[i]['titles']:
                results = json.loads(thenewsapi(args.api_key, t, args.start_date, args.end_date))
                json.dump(results, f, indent=4)

    if args.tsv: convert_to_tsv(args, contents)

if __name__ == "__main__":
    collector()