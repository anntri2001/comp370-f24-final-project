### How to run the scripts
Navigate to root of project, and run the following command:
```
python -m newscover.collector -k <api_key> -i <input_json> -o <output_json> -t <output_tsv>
```
The input json file is of the format:
```
{
    'key': 'title to search'
    ...
}
```
To change the dates searched, navigate to collector.py and comment out or add dates in the published_dates variable.

As output the columns are as follows:
```
['uuid', 'title', 'snippet', 'published_at', 'locale', 'source', 'url', 'relevance_score', 'keywords']
```