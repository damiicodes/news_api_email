import requests

api_key = 'pub_2203420aae6659fc0fdafc55040829e9c0ff0'
url = 'https://newsdata.io/api/1/news?api' \
      'key=pub_2203420aae6659fc0fdafc55040829e9c0ff0&q=ChatGPT&language=en'
# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access article title and description
for article in content['results']:
    print(article['title'])
    print(article['description'])


