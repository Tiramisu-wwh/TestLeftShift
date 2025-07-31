import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200 and response.json().get("userId") == 1:
    print("成功！")
else:
    print("失败！")