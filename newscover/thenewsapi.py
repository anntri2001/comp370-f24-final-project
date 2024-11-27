import requests
import json

# API_URL = 'https://api.thenewsapi.com/v1/news/all/'
API_URL = 'https://api.thenewsapi.com/v1/news/top/'
objects = ['uuid', 'title', 'snippet', 'published_at', 'locale', 'source', 'url', 'relevance_score']
language = 'en'
locale = 'us,ca'
categories = 'entertainment'
search_fields = 'title'
exclude_domains = 'https://rlsbb.cc/,https://ohnotheydidnt.livejournal.com/,https://yts.mx/'

def fetch_news_articles(api_key, keywords, published_date):
    params = {
        'api_token': api_key,
        'search': keywords,
        'published_on': published_date,
        'search_fields': search_fields,
        'language': language,
        'locale': locale,
        'categories': categories,
        'exclude_domains': exclude_domains,
        'sort': 'relevance_score'
    }

    response = requests.get(API_URL, params)
    response.raise_for_status()
    data = response.json()

    return data['data']

def extract_response(data, keywords):
    filtered_objects = [
        {key: d[key] for key in objects if key in d} 
        for d in data
        ]

    for i in filtered_objects:
        i['keywords'] = keywords

    filtered_json = json.dumps(filtered_objects, indent=4)

    return filtered_json

def thenewsapi(api_key, keywords, published_on):
    data = fetch_news_articles(
        api_key, 
        keywords, 
        published_on
        )

    return extract_response(data, keywords)

if __name__ == '__main__':
    response = thenewsapi('AaV484hefgrCAc1CRjodqbgO5WQk0vLdCOw4zjI0', "Bad Boys: Ride or Die", '2024-06-01', '2024-06-30')
    print(response)