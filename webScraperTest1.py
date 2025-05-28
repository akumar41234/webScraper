from bs4 import BeautifulSoup
import json

with open("index.html", "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
data = []

# Loop through top-level sections like Address4, Address6, etc.
sections = soup.find_all("section", class_="p2 mb2 clearfix bg-white minishadow")

for section in sections:
    header = section.find("h3")
    if not header:
        continue
    section_name = header.text.strip()

    methods = []
    method_divs = section.find_all("div", class_="border-bottom")
    for method_div in method_divs:
        name_div = method_div.find("span", class_="code strong strong truncate")
        desc_div = method_div.find("p")

        name = name_div.text.strip() if name_div else ""
        description = desc_div.text.strip() if desc_div else ""

        if name:
            methods.append({"name": name, "description": description})

    if methods:
        data.append({
            "section": section_name,
            "methods": methods
        })

with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Data extraction completed. Saved to data.json")
