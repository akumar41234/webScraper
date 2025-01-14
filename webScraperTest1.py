from bs4 import BeautifulSoup
import json

with open("index.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
data = []

divs = soup.find_all("div", class_="a-section a-spacing-none octopus-pc-item-block octopus-pc-asin-block")

for div in divs:
    img_tag = div.find("a", class_="a-link-normal octopus-pc-item-link")
    link = img_tag.img["src"] if img_tag and img_tag.img else ""
    span_title = div.find("span", class_="a-size-base a-color-base")
    title = span_title.text.strip() if span_title else ""
    span_rating = div.find("span", class_="a-icon-alt")
    rating = span_rating.text.strip() if span_rating else ""
    span_price = div.find("span", class_="a-price-whole")
    price = span_price.text.strip() if span_price else ""
    data.append({"link": link, "title": title, "rating": rating, "price": price})

with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Data extraction completed. Saved to data.json")
