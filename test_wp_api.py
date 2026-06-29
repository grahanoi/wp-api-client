from wp_api import WPClient

client = WPClient(base_url="https://wptavern.com/")

# List published posts, number of post here 5, chose page 1 or 2, orderby
posts = client.posts.list(status="publish", per_page=5, page=1, orderby="date")
for post in posts:
    print(post['id'], post['title']['rendered'])