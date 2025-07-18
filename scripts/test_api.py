import requests

# Step 1: Get JWT token
token_url = "http://127.0.0.1:8000/api/token/"
credentials = {
    "email": "mishradiwasbrijesh@gmail.com",
    "password": "Admin@123"
}
token_response = requests.post(token_url, json=credentials)
tokens = token_response.json()
access_token = tokens.get("access")

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Step 2: GET articles
get_url = "http://127.0.0.1:8000/api/articles/"
get_response = requests.get(get_url, headers=headers)
print("GET response:", get_response.json())

# Step 3: POST new article
post_data = {
    "title": "Sample Article",
    "slug": "sample-article",
    "content": "This is some test content.",
    "author": 1  # or whatever the current user ID is
}
post_response = requests.post(get_url, headers=headers, json=post_data)
print("POST response:", post_response.json())

# Step 4: DELETE article with ID 1
delete_url = "http://127.0.0.1:8000/api/articles/1/"
delete_response = requests.delete(delete_url, headers=headers)
print("DELETE response:", delete_response.status_code)
