import requests
import threading
from tqdm import tqdm

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def obtener_datos_pokemon(pokemon_id):
    try:
        response = requests.get(f"{BASE_URL}{pokemon_id}")
        if response.status_code == 200:
            datos = response.json()
            nombre = datos["name"].capitalize()
            tipos = [tipo["type"]["name"].capitalize() for tipo in datos["types"]]
            estadisticas = {stat["stat"]["name"]: stat["base_stat"] for stat in datos["stats"]}
            imprimir_datos_pokemon(nombre, tipos, estadisticas)
        else:
            print(f"Error al obtener el Pokémon {pokemon_id}: {response.status_code}")
    except requests.RequestException as e:
        print(f"Excepción al obtener el Pokémon {pokemon_id}: {e}")

def imprimir_datos_pokemon(nombre, tipos, estadisticas):
    print(f"Nombre: {nombre}")
    print(f"Tipo: {', '.join(tipos)}")
    print("Estadísticas:")
    print(f"  HP: {estadisticas.get('hp', 'N/A')}")
    print(f"  Ataque: {estadisticas.get('attack', 'N/A')}")
    print(f"  Defensa: {estadisticas.get('defense', 'N/A')}")
    print(f"  Ataque especial: {estadisticas.get('special-attack', 'N/A')}")
    print(f"  Defensa especial: {estadisticas.get('special-defense', 'N/A')}")
    print(f"  Velocidad: {estadisticas.get('speed', 'N/A')}")
    print("-" * 40)

def main():
    cantidad_pokemon = 50
    hilos = []
    for pokemon_id in range(1, cantidad_pokemon + 1):
        hilo = threading.Thread(target=obtener_datos_pokemon, args=(pokemon_id,))
        hilos.append(hilo)
        hilo.start()

    for hilo in tqdm(hilos, desc="Obteniendo datos de Pokémon"):
        hilo.join()

if __name__ == "__main__":
    main()
