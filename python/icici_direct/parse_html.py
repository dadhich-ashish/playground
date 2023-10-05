from bs4 import BeautifulSoup
import requests

# Make a request to the website
#url = 'https://example.com'
#response = requests.get(url)
with open('python\icici_direct\icici_direct.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
    
# Parse the HTML content of the page
soup = BeautifulSoup(html_content, 'html.parser')
print("someting working or not?")
# Find specific elements using patterns
# For example, to find all <a> tags with class 'example-link':
allIdeas = soup.find_all('div', class_='copyable-text')

# Iterate through the found elements and extract data
for idea in allIdeas:
   companyName = idea.find_all('strong')
   print(companyName)
# You can use similar methods to find other elements and extract data as per your pattern.
