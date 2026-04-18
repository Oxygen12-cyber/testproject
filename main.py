import requests
from fastapi import FastAPI


app = FastAPI()


def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes
        
        posts = response.json()
        print(f"Successfully fetched {len(posts)} posts.\n")
        print("Here are the first 5 posts:\n" + "-"*40)
        return posts
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

@app.get('/')
def RootPage():
    return fetch_posts()


