import requests

url = "http://www.google.com"

# set up variable that does a GET against the given address
response = requests.get(url)

# will show response code
print(response)

# print out source text for given url
print(response.text)