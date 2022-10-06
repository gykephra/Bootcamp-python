
mot = input("Tapez un mot: ")
mot = {lettre : [mot.index(lettre) for i in lettre] for lettre in mot}
print(mot)

#exo2
wallet= 1000
items_purchase = {
  "Water": 1,
  "Bread": 3,
  "TV": 1,
  "Fertilizer": 20
}
articlpayable=[article for article in items_purchase if items_purchase [article]<=wallet]
print(articlpayable)