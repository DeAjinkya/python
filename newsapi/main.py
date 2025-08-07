import requests

query = input("what are u looking for today? ")

api = "8f7eda7470c44514b5365a3bc2aae118"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-06&to=2025-08-06&sortBy=popularity&apiKey={api}"

r = requests.get(url)
data = r.json()
articles = data["articles"]

for index,article in enumerate(articles):
    print(index + 1,article["title"],article["url"])
    print("\n***************************\n")

