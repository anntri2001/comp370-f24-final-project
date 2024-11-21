import requests
import json

API_URL = 'https://api.thenewsapi.com/v1/news/all/'
objects = ['uuid', 'title', 'published_at', 'url']
language = 'en'
limit = 10

def fetch_news_articles(api_key, keywords, startdate, enddate):
    params = {
        'api_token': api_key,
        'search': keywords,
        'language': language,
        'published_after': startdate,
        'published_before': enddate,
        'limit': limit
    }

    response = requests.get(API_URL, params)
    response.raise_for_status()
    data = response.json()

    return data['data']

def extract_response(data):
    filtered_objects = [
        {key: d[key] for key in objects if key in d} 
        for d in data
        ]

    filtered_json = json.dumps(filtered_objects, indent=4)
    return filtered_json

def thenewsapi(api_key, keywords, startdate, enddate):
    data = fetch_news_articles(
        api_key, 
        keywords, 
        startdate, 
        enddate
        )

    return extract_response(data)

if __name__ == '__main__':
    pass