import json
import requests
import os
import xml.etree.ElementTree as ET
import re

FEED_DIR = "feeds"

import os
import re
import requests
import xml.etree.ElementTree as ET

FEED_DIR = "feeds"  # make sure this is defined somewhere globally or adjust accordingly

def fetch_and_save(name, url):
    try:
        print(f"Fetching: {url}")
        r = requests.get(url)
        r.raise_for_status()
        os.makedirs(FEED_DIR, exist_ok=True)

        # Parse the XML content
        root = ET.fromstring(r.text)

        # Modify the <title> and <description> in the <channel>
        channel = root.find("channel")
        if channel is not None:
            # Clean the <channel><title>
            title_elem = channel.find("title")
            if title_elem is not None:
                stripped_title = re.sub(r" - [^-]+$", "", title_elem.text or "")
                title_elem.text = stripped_title

            # Update the <channel><description>
            desc_elem = channel.find("description")
            if desc_elem is not None:
                desc_elem.text = f"Custom RSS feed for {name}"

            # Loop through <item>s and clean each <title>
            for item in channel.findall("item"):
                item_title_elem = item.find("title")
                if item_title_elem is not None:
                    original_title = item_title_elem.text or ""
                    stripped_item_title = re.sub(r" - [^-]+$", "", original_title)
                    item_title_elem.text = stripped_item_title

        # Save to file
        filename = os.path.join(FEED_DIR, f"{name}.xml")
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

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
