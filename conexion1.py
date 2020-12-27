import requests

def conexion():
    r = requests.get('https://api.nasa.gov/neo/rest/v1/feed?api_key=ooyOyfc1LD91FDtXEpzSscSOH8m6Iaq0QDaCFgX7')
    respuesta=r.json()
    return respuesta["near_earth_objects"]

# r = requests.get('https://api.nasa.gov/neo/rest/v1/feed?api_key=ooyOyfc1LD91FDtXEpzSscSOH8m6Iaq0QDaCFgX7')
# respuesta=r.json()
# asteroides=respuesta["near_earth_objects"]

try:
    asteroides = conexion()
except:
    print("No se pudo realizar conexion")
else:
    resp_keys= dict.keys(asteroides)
    resp_keys= dict.keys(asteroides)
    resp_id=[]
    resp_name=[]
    resp_hazardous=[]
    diameter_min=[]
    diameter_max=[]
    for resp_keys in asteroides:
        r2 = asteroides[resp_keys]
        #r3 = r2[0]
        k=0
        while k<=10:
            asteroide = r2[k]
            resp_id.append(asteroide['id'])
            resp_name.append(asteroide['name'])
            diameter=asteroide['estimated_diameter']
            kilometers=diameter['kilometers']
            diameter_min.append(kilometers['estimated_diameter_min'])
            diameter_max.append(kilometers['estimated_diameter_max'])
            resp_hazardous.append(asteroide["is_potentially_hazardous_asteroid"])
            k+=1
    long = 0
    lim1 = len(resp_id)

    while long < lim1:
        print(f"ID del asteroide: {resp_id[long]}")
        print(f"Nombre del asteroide: {resp_name[long]}")
        print(f"Diametro min (Km): {diameter_min[long]}")
        print(f"Diametro max (Km): {diameter_max[long]}")
        print(f"Potencialmente Peligroso: {resp_hazardous[long]}")
        long+=1


#print(resp_id[0])
    
