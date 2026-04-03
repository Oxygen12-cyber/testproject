import json
from callapi import get_posts


def main():
    try:
        posts = get_posts()
        output = {
            "status": "success",
            "count": len(posts),
            "posts": posts,
        }
    except Exception as e:
        output = {
            "status": "error",
            "message": str(e),
        }
    print(json.dumps(output))


if __name__ == "__main__":
    main()
