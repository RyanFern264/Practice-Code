from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

all_tags = soup.find_all("a", class_="storylink")
all_span = soup.find_all(name="span", class_="score")

for span in all_span:
    print(span.text)

# for tag in all_tags:
#     print(tag)
#     # print(tag.text)
#     # print(tag['href'])

# with open("website.html") as html:
#     html_lines = html.read()
#
# soup = BeautifulSoup(html_lines, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)