import requests

# Задание 1: Получение данных
url = "https://api.github.com/search/repositories"
params = {"q": "language:html"}
response = requests.get(url, params=params)
print("Status code:", response.status_code)
print("Response JSON:", response.json())

# Задание 2: Параметры запросов
url_posts = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url_posts, params={"userId": 1})
print("Filtered Posts:", response.json())

# Задание 3: Отправка данных
url_create_post = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post(url_create_post, json=data)
print("POST Status Code:", response.status_code)
print("POST Response JSON:", response.json())
