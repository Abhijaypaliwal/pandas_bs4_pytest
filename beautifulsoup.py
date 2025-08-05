#beautifulsoup is a library to extract info from HTML and XML docs
# think like webpage like HTML tree and beautiful soup will help u to climb the tree and pluck only the elements u need
# from it

# we cannot use it to make request
# it is only to proceess extracted data from the HTML content you already fetched

from bs4 import BeautifulSoup
import requests

#url = "https://rahulshettyacademy.com/angularpractice/"
url = "https://rahulshettyacademy.com/AutomationPractice/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# WOULD PRINT THE WHOLE HTML
#print(soup.prettify())
title = soup.title
print(title.text)
first_link = soup.find('a')
all_links = soup.find_all('a')

for link in all_links:
    print(link.get('href'))
# find by class
# all_links = soup.find_all('div', class_='header')
#
# #find by ID
# soup.find(id="main-content")
#
# #find by attribute
# soup.find_all(attrs={"data-role": "button"})

# display the radio buttons

url = "https://rahulshettyacademy.com/AutomationPractice/"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
radio_buttons = soup.find_all('input', {'type':'radio'})
print(radio_buttons)
for i, radio in enumerate(radio_buttons, start = 1):
    value = radio.get('value')
    print(f"option {i}: {value}")

