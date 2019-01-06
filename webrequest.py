import requests

url = "http://www.google.com"

# set up variable that does a GET against the given address
response = requests.get(url)

# will show response code
print(response)

# print out source text for given url
print(response.text)


url = "http://httpbin.org/post"
# data to be provided in POST, can take multiple forms but here I just use a string
mydata = "data to pass"
# use post verb
response = requests.post(url,data=mydata)
print(response.text)