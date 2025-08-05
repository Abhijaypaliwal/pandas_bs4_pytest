#COMBINES THE REQUEST LIBRARY WITH HTML PARSING CAPABILITIES OF BEAUTIFULSOUP
#SUPPORTS JAVA REDNDRING ALSO

from requests_html import HTMLSession
from requests.auth import HTTPBasicAuth

# Create a session
session = HTMLSession()

# Send a GET request
response = session.get("https://www.google.com")

# Print HTTP status code
print(response.status_code)  # e.g. 200 = OK

# Print raw response content (HTML)
#print(response.text)  # same as response.html.html

params = {'key1': 'value1', 'key2': 'value2'}
response = session.get("https://rahulshettyacademy.com/AutomationPractice/", params=params)
print(response.url) #show full URL with params

# username = ('abhijaypaliwal')
# password = ('<PASSWORD>')
# #response = session.get('https://api.github.com/user', auth=HTTPBasicAuth(username, password))
# print(response.json())
# print(response.status_code)

title_tag = response.html.find('title', first=True)
print("Page Title:", title_tag.text if title_tag else "No title found")

# ✅ 2. Get the first <a> tag and its href
first_link = response.html.find('a', first=True)
if first_link:
    print("\nFirst Link Text:", first_link.text.strip())
    print("First Link HREF:", first_link.attrs.get('href'))
else:
    print("\nNo <a> tag found")

# ✅ 3. Get all <a> tags
all_links = response.html.find('a')
print(f"\nTotal <a> tags found: {len(all_links)}")

for i, link in enumerate(all_links, start=1):
    href = link.attrs.get('href')
    text = link.text.strip()
    print(f"{i}. {text} → {href}")