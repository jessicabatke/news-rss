import json
import requests
import os

def fetch_and_save(name, url):
    try:
        print(f"Fetching: {url}")
        r = requests.get(url)
        r.raise_for_status()
        filename = f"{name}.xml"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(r.text)
        return filename
    except Exception as e:
        print(f"Failed to fetch {name}: {e}")
        return None

def generate_index(feed_names):
    with open("index.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Custom RSS Feeds</title>\n</head>\n<body>\n")
        f.write("<h1>Custom RSS Feeds</h1>\n<ul>\n")
        for name in sorted(feed_names):
            f.write(f'<li><a href="{name}.xml">{name}</a></li>\n')
        f.write("</ul>\n</body>\n</html>")

def main():
    with open("feeds.json", "r") as f:
        feeds = json.load(f)

    saved = []
    for name, url in feeds.items():
        result = fetch_and_save(name, url)
        if result:
            saved.append(name)

    generate_index(saved)

if __name__ == "__main__":
    main()
