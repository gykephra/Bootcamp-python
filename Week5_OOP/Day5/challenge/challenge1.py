def tempsChargement(site):
    import requests
    import time

    debut = time.time()
    requests.get(site)
    temps= time.time() - debut
    return temps

def resultat(site,temps):
    print(f"Le temps de Chargement de {site} est ==> {temps}")

resultat("https://www.google.com/",tempsChargement("https://www.google.com/"))
resultat("https://www.imdb.com/",tempsChargement("https://www.imdb.com/"))
resultat("https://www.ynet.com/",tempsChargement("https://www.google.com/"))
