import tweepy
import csv

# Authenticate to Twitter
auth = tweepy.OAuthHandler("sbnbAjafkj088eFdHzeAHG4R5", "L3Sg4aJbXXqzwesAo16Pdzp2bmX6O7dlHBP7Bcx2fE9qqPVcAl")
auth.set_access_token("1438889782545985541-9Scf68wbFZE0LdSXnHfZ6zSZp2F1MY", "hwrTplwCQloueEq4zudVRK0FRpDGk7Yi7TMUtq3o607ry")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

id_sitio = 0
nombre_sitio = 'kike'
filas_guardar = []

id = None
count = 0

for tweet in tweepy.Cursor(api.search, q=nombre_sitio, lang = 'es').items(5):
    fila = [id_sitio, nombre_sitio, tweet.text]
    filas_guardar.append(fila)
    count = count + 1
    print(f"{count}->{tweet.user.name}:{tweet.text}")

with open('tuits.csv', 'w', encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';', )
    writer.writerows(filas_guardar)





#Más en https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials