import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("a")

for title in titles[:10]:

    print(title.text)