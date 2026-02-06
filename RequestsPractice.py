import requests


# GET
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
post = response.json()
print(post)

# POST
new_post = {"title": "Hello", "body": "World", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

# PUT
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_post)

# DELETE
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")