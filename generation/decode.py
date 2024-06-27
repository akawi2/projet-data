import json

from generation.model import Client, Ville

def decode_json():
    clients = []
    villes = []

    # Ouvre le fichier data.json et charge les données
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Affiche les informations sur les villes
    print("Informations sur les villes :")
    for ville in data['villes']:
        villeObj = Ville(ville['x'], ville['y'], ville['id'])
        villes.append(villeObj)
        print(f"Ville {ville['id']} : ({ville['x']}, {ville['y']}) avec {len(ville['voisins'])} voisins")

    # Affiche les informations sur les clients
    print("\nInformations sur les clients :")
    for client in data['clients']:
        ville = next(v for v in data['villes'] if v['id'] == client['ville'])
        clientObj = Client(ville, client['charge'], client['open_time'], client['close_time'])
        clients.append(clientObj)

        print(f"Client dans la ville {client['ville']} (à la position ({ville['x']}, {ville['y']})) avec une charge de {client['charge']} et des heures d'ouverture de {client['open_time']} à {client['close_time']}")
    return villes, clients