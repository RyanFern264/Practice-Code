from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

all_tags = soup.find_all("a", class_="storylink")
all_span = soup.find_all(name="span", class_="score")

for i in range(len(all_tags)):
    print(all_tags[i].text)
    print(all_tags[i]['href'])
    print(all_span[i].text)
    print("\n")



# with open("website.html") as html:
#     html_lines = html.read()
#
# soup = BeautifulSoup(html_lines, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)