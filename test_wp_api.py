from wp_api import WPClient

client = WPClient(base_url="https://imaginatic.es")

# List published posts, number of post here 5, chose page 1 or 2
posts = client.posts.list(status="publish", per_page=5, page=2)
for post in posts:
    print(post['id'], post['title']['rendered'])