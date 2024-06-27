import random
import matplotlib.pyplot as plt
import numpy as np
import json

from generation.model import Client, Ville


def generer_villes(nb_villes, largeur, hauteur):
    villes = []
    id = 0
    for _ in range(nb_villes):
        id += 1
        x = random.uniform(0, largeur)
        y = random.uniform(0, hauteur)
        villes.append(Ville(x, y, id))

    # Créer les connexions entre les villes
    for ville in villes:
        nb_connexions = random.randint(2, 5)
        for _ in range(nb_connexions):
            autre_ville = random.choice(villes)
            if autre_ville != ville:
                if autre_ville in ville.voisins:
                    pass
                else :
                    ville.voisins.append(autre_ville)
                    autre_ville.voisins.append(ville)

    # Fermer le cycle eulérien
    villes[0].voisins.append(villes[-1])
    villes[-1].voisins.append(villes[0])

    return villes

def generer_clients(villes, nb_clients_par_ville, start_time, end_time, mean_service_time, std_service_time):
    clients = []
    for ville in villes:
        for _ in range(nb_clients_par_ville):
            charge = random.randint(1, 10)
            open_time = random.uniform(start_time, end_time)
            service_time = np.random.normal(mean_service_time, std_service_time)
            close_time = open_time + service_time
            client = Client(ville, charge, open_time, close_time)
            clients.append(client)
    return clients

def tracer_graphe(villes):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_title("Graph respectant le cycle eulérien")

    # Tracer les villes
    for i in range(0, len(villes)):
        if i == 0:  
            ax.plot(villes[i].x, villes[i].y, 'ro', markersize=10)
        else: 
            ax.plot(villes[i].x, villes[i].y, 'bo', markersize=10)


    # Tracer les arêtes
    for ville in villes:
        for voisin in ville.voisins:
            ax.plot([ville.x, voisin.x], [ville.y, voisin.y], 'k-')

    plt.show()

# Test d'utilisation
nb_villes = 2
nb_clients_par_ville = 1
start_time = 8  # 8h
end_time = 18   # 18h
mean_service_time = 0.5  # 30 minutes
std_service_time = 0.1   # 10 minutes
villes = generer_villes(nb_villes, 100, 100)
clients = generer_clients(villes, nb_clients_par_ville, start_time, end_time, mean_service_time, std_service_time)
list_villes = []
list_clients = []
for ville in villes:
    list_villes.append([ville.id, ville.x, ville.y])

# Création du fichier JSON
data = {
    "villes": [],
    "clients": []
}

for ville in villes:
    data["villes"].append({
        "id": ville.id,
        "x": ville.x,
        "y": ville.y,
        "voisins": [v.id for v in ville.voisins]
    })

for client in clients:
    data["clients"].append({
        "ville": client.ville.id,
        "charge": client.charge,
        "open_time": client.open_time,
        "close_time": client.close_time
    })

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
    
print(list_villes)
tracer_graphe(villes)