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
