import requests

response = requests.get("https://www.google.com")
print(response.status_code)
# print(response.text[:300])

response = requests.get("https://www.google.com", stream=True)
# print(response.raw.read()[:100])
print(response.request.headers["Accept-Encoding"])
# gzip, deflate
print(response.headers["Content-Encoding"])
# gzip
print(response.ok)
# True
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))

# will raise HTTPError exception only if the response was unsuccessful
response.raise_for_status()

params = {"search": "grey kitten", "max_results": 15}

response = requests.get("https://www.google.com", params=params)
print(response.request.url)

data = {"description": "white kitten", "name": "Snowball", "age_months": 6}
# response = requests.post("https://www.google.com", data=data)
response = requests.post("https://www.google.com", json=data)
print(response.request.url)
print(response.request.body)
