from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article = soup.find_all(name="a", class_="titlelink")


class_score = soup.find(name="td", class_="subtext")
score = class_score.get_text()
points = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
maximum = max(points)
uo = points.index(maximum)

print(article[uo])