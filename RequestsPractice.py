import requests

base_url = "https://jsonplaceholder.typicode.com"
# GET all posts
response = requests.get(f"{base_url}/posts")
posts = response.json()

# GET a single post
response = requests.get(f"{base_url}/posts/1")
post = response.json()

# GET posts by user
response_by_user = requests.get(f"{base_url}/posts?userId=1")
post_by_user = response_by_user.json()

# GET nested resources
response_nested_resources = requests.get(f"{base_url}/posts/1/comments")
post_nested_resources = response_nested_resources.json()

# POST requests
new_post = {
    "title": "My New Post",
    "body": "This is the content of my post.",
    "userId": 1
}
response = requests.post(f"{base_url}/posts", json=new_post)

# Replace a post : PUT
updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "Completely new content.",
    "userId": 1
}
response = requests.put(f"{base_url}/posts/1", json=updated_post)

# partial update : PATCH
partial_update = {"title": "Only the Title Changed"}
response = requests.patch(f"{base_url}/posts/1", json=partial_update)

# DELETE
response = requests.delete(f"{base_url}/posts/1")

