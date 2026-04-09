import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes
        
        posts = response.json()
        print(f"Successfully fetched {len(posts)} posts.\n")
        print("Here are the first 5 posts:\n" + "-"*40)
        
        for post in posts[:5]:
            print(f"ID: {post.get('id')}")
            print(f"Title: {post.get('title')}")
            print(f"Body: {post.get('body')}")
            print("-" * 40)
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_posts()
