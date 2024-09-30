# https://discuss.python.org/t/on-macos-14-pip-install-throws-error-externally-managed-environment/50352/6

# pip install requests
# pip install arrow
# pip install Pillow # for Windows and Mac OS
# pip install pandas

import requests
import arrow
import PIL.Image
import pandas

response = requests.get("http://www.google.com")
print(len(response.text))

date = arrow.get("2024-09-30", "YYYY-MM-DD")
print(date.shift(weeks=+6).format("MMM DD YYYY"))

image = PIL.Image.open("profile.jpg")
print(image.size)
print(image.format)

visitors = [1235, 6424, 9345, 8464, 2345]
errors = [23, 45, 33, 45, 76]
df = pandas.DataFrame(
    {"visitors": visitors, "errors": errors},
    index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
)
print(df)
print("Mean of errors", df["errors"].mean())
