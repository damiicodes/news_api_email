import requests

api_key = 'pub_2203420aae6659fc0fdafc55040829e9c0ff0'
url = 'https://newsdata.io/api/1/news?api' \
      'key=pub_2203420aae6659fc0fdafc55040829e9c0ff0&q=ChatGPT&language=en'
# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# for article in content['results']:
#     if article['title'] is None or article['description'] is None\
#             or article['link'] is None:
#           print(article)

# Access article title and description
body = ''
for article in content['results']:
      if article['description'] is not None:
            body = body + article['title'] + '\n' \
            + article['description'] \
            + '\n' + article['link'] + 2*'\n'

print(body)




