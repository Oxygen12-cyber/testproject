import requests

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    try:
        posts = get_posts()
        print(f"Got {len(posts)} posts")
        print(posts[:3])  # preview first 3 items
    except requests.RequestException as err:
        print("API request failed:", err)