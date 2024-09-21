from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

article_titles = soup.find_all("a", class_="storylink")
first_article_tag = article_titles[0]
first_article_upvote = soup.find("span", class_="score").get_text()

article_texts = []
article_links = []


for tag in article_titles:
    text = tag.get_text()
    article_texts.append(text)
    link = tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name='span', class_="score")]


print(article_texts)
print(article_links)
print(article_upvotes)

Largest_upvotes = max(article_upvotes)
index_of_greatest = article_upvotes.index(Largest_upvotes)

print(Largest_upvotes)
print(index_of_greatest)

print(article_texts[index_of_greatest])
print(article_links[index_of_greatest])


# print(first_article_tag)
# print(first_article_tag.get_text())
# print(article_titles[0].get("href"))
# print(article_titles[0].get_text())
#
# print(first_article_upvote)














# # Open the file with the correct encoding
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup)
# # print(soup.prettify())
# print(soup.li.string)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.get_text())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading").get_text()
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)

