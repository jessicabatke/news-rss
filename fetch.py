import json
import requests

def fetch_and_save(name, url):
    try:
        print(f"Fetching: {url}")
        r = requests.get(url)
        r.raise_for_status()
        with open(f"{name}.xml", "w", encoding="utf-8") as f:
            f.write(r.text)
    except Exception as e:
        print(f"Failed to fetch {name}: {e}")

def main():
    with open("feeds.json", "r") as f:
        feeds = json.load(f)

    for name, url in feeds.items():
        fetch_and_save(name, url)

if __name__ == "__main__":
    main()
