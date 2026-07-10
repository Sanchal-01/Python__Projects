import requests

# query = "Artificial Intelligence"

# Improved query
query = input("What do you want to study today about : ")

api = " Get your personal api key from https://newsapi.org/ "

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-06-08&sortBy=publishedAt&apiKey={api}"

# print(url)   
# We can have the url of the news in the terminal for our above query.
# If we get the url and go to that link we can get news in the form of json which is not human readable...so we can use any extension like json preety to convert the json into human readable format.



# Otherwise we can have the entire news in to are terminal via :

r = requests.get(url)
data = r.json()

articles = data ["articles"]
for index,article in enumerate(articles):        # Here I have used enumerate to get the index number of the news along with title and url link. 
    print(index + 1, article["title"],"\n", article["url"])

    print("===================================================\n")