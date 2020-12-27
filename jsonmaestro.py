import requests

r = requests.get('https://api.nasa.gov/neo/rest/v1/feed?api_key=ooyOyfc1LD91FDtXEpzSscSOH8m6Iaq0QDaCFgX7')
respuesta=r.json()

print(respuesta)