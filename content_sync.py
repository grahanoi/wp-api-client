from wp_api import WPClient
from wp_api.auth import ApplicationPasswordAuth

# Using Application Passwords (recommended)
auth = ApplicationPasswordAuth(username="noirin", app_password="WmX5 IHp8 5XYN jByj vqD4 nPLN")
client = WPClient(base_url="https://imaginatic.es", auth=auth)

# Get all published posts
posts = client.posts.list(status="publish")
print(f"Title: {posts[0]['title']['rendered']}")

# Get all media
media_items = client.media.list()
print(f"Media Count: {len(media_items)}")