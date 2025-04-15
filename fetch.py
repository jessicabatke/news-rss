import json
import requests
import os

FEED_DIR = "feeds"

def fetch_and_save(name, url):
    try:
        print(f"Fetching: {url}")
        r = requests.get(url)
        r.raise_for_status()
        os.makedirs(FEED_DIR, exist_ok=True)
        filename = os.path.join(FEED_DIR, f"{name}.xml")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(r.text)
        return name
    except Exception as e:
        print(f"Failed to fetch {name}: {e}")
        return None

def generate_index(feed_names):
    base_url = "https://jessicabatke.github.io/news-rss/feeds/"  # Replace with your actual URL
    with open("index.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>RSS Feed URLs</title>\n</head>\n<body>\n")
        f.write("<h1>RSS Feed URLs (copy these into your reader)</h1>\n")
        for name in sorted(feed_names):
            full_url = f"{base_url}{name}.xml"
            f.write(f"<div><code>{full_url}</code></div>\n")
        f.write("</body>\n</html>")



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
