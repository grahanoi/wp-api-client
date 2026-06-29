"""from wp_api import WPClient

client = WPClient(base_url="https://imaginatic.es")

# List published posts, number of post here 5, chose page 1 or 2, orderby
posts = client.posts.list(status="publish", per_page=1, page=1, orderby="date")
for post in posts:
    print(post['id'], post['title']['rendered'], post['date'][:10], post['content']['rendered'], post['link'], post['author'])  # Print first 100 characters of content """


# TODO: Get API User name and password
# TODO: hero, language and partner fields are not available in the API, so we need to find a way to get them. 
# TODO: Use same description body as the website
# TODO: Automatically generate the YAML front matter for each post, including the hero image, language, and partner fields.
# TODO: Implement a function that creats a new page in the Cotedi Repo


from wp_api import WPClient
from html.parser import HTMLParser
import re

# Simple HTML stripper 
class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_data(self, data):
        self.text.append(data)
    def get_text(self):
        return ''.join(self.text).strip()
# removes the Elementor HTML tags for plain text for the description/body
def strip_html(html):
    stripper = HTMLStripper()
    stripper.feed(html)
    return stripper.get_text()

client = WPClient(base_url="https://imaginatic.es")
posts = client.posts.list(status="publish", per_page=5, page=1, orderby="date")

for post in posts:
    post_id   = post['id']
    title     = post['title']['rendered']
    date      = post['date'][:10]  # just the YYYY-MM-DD part
    content   = strip_html(post['content']['rendered'])
    link      = post['link']
    #language  = post['language']

    # Fetch author name
    author_id = post['author']
    author    = client.users.get(author_id)
    author_name = author['name']
    media_items = client.media.list()

    yaml = f"""---
title: {title}
author: {author_name}
date: {date}
type: news
tags:
- news
hero: {media_items[0]['source_url'] if media_items else 'No image available'}
link: {link}
partner:
language:
description: |
  {content[:200]}...
---
{content}
"""
    print(yaml)
    print("---")

