import random


def crearEntrenador(tupla):
    entrenador = input("Ingrese el nombre del entrenador: ")
    pokemon = input("Ingrese el nombre del Pokemon: ")

    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)

    nuevo = (entrenador, pokemon, ataque, vida)
    tupla.append(nuevo)

    print("Entrenador y Pokemon creados correctamente.")
    print("Ataque:", ataque)
    print("Vida:", vida)


def listaEntrenador(tupla):
    if len(tupla) == 0:
        print("No hay entrenadores registrados.")
        return

    # Metodo de burbuja por ataque
    for pasada in range(len(tupla)):
        anterior = None

        for actual in range(len(tupla)):
            if anterior is not None:
                if tupla[anterior][2] > tupla[actual][2]:
                    aux = tupla[anterior]
                    tupla[anterior] = tupla[actual]
                    tupla[actual] = aux

            anterior = actual

    print("\n===== LISTA DE ENTRENADORES =====")

    for numero, pokemon in enumerate(tupla, 1):
        entrenador = pokemon[0]
        nombre = pokemon[1]
        ataque = pokemon[2]
        vida = pokemon[3]

        print(
            numero,
            ". Entrenador:",
            entrenador,
            "| Pokemon:",
            nombre,
            "| Ataque:",
            ataque,
            "| Vida:",
            vida,
        )


def busquedaBinaria(lista, vidaBuscada):
    if len(lista) == 0:
        return None

    medio = len(lista) // 2

    if lista[medio][3] == vidaBuscada:
        return lista[medio]

    if vidaBuscada < lista[medio][3]:
        izquierda = lista[:medio]
        return busquedaBinaria(izquierda, vidaBuscada)

    derecha = lista[medio:]
    derecha.pop(0)

    return busquedaBinaria(derecha, vidaBuscada)


def borraPorPokemon(tupla):
    if len(tupla) == 0:
        print("No hay Pokemon registrados.")
        return

    vidaBuscada = int(input("Ingrese la vida que desea buscar: "))

    # Metodo de seleccion por vida
    for posicion in range(len(tupla)):
        menor = posicion

        for siguiente in range(posicion, len(tupla)):
            if tupla[siguiente][3] < tupla[menor][3]:
                menor = siguiente

        aux = tupla[posicion]
        tupla[posicion] = tupla[menor]
        tupla[menor] = aux

    encontrado = busquedaBinaria(tupla, vidaBuscada)

    if encontrado is not None:
        tupla.remove(encontrado)

        print("Pokemon eliminado:")
        print("Entrenador:", encontrado[0])
        print("Pokemon:", encontrado[1])
    else:
        print("No se encontro un Pokemon con esa vida.")


def peleaPokemon(lista):
    if len(lista) < 2:
        print("Se necesitan al menos 2 Pokemon para pelear.")
        return

    listaEntrenador(lista)

    numero1 = int(input("Ingrese el numero del primer Pokemon: "))
    numero2 = int(input("Ingrese el numero del segundo Pokemon: "))

    if numero1 == numero2:
        print("Debe seleccionar dos Pokemon diferentes.")
        return

    pokemon1 = None
    pokemon2 = None

    for numero, pokemon in enumerate(lista, 1):
        if numero == numero1:
            pokemon1 = pokemon

        if numero == numero2:
            pokemon2 = pokemon

    if pokemon1 is None or pokemon2 is None:
        print("Numero de Pokemon invalido.")
        return

    entrenador1 = pokemon1[0]
    nombre1 = pokemon1[1]
    ataque1 = pokemon1[2]
    vida1 = pokemon1[3]

    entrenador2 = pokemon2[0]
    nombre2 = pokemon2[1]
    ataque2 = pokemon2[2]
    vida2 = pokemon2[3]

    multiplicador1 = random.randint(0, 5)
    multiplicador2 = random.randint(0, 5)

    dano1 = ataque1 * multiplicador1
    dano2 = ataque2 * multiplicador2

    vidaFinal1 = vida1 - dano2
    vidaFinal2 = vida2 - dano1

    if vidaFinal1 < 0:
        vidaFinal1 = 0

    if vidaFinal2 < 0:
        vidaFinal2 = 0

    print("\n===== PELEA POKEMON =====")
    print(nombre1, "ataca con", dano1, "de daño.")
    print(nombre2, "ataca con", dano2, "de daño.")

    print(nombre1, "queda con", vidaFinal1, "de vida.")
    print(nombre2, "queda con", vidaFinal2, "de vida.")

    if vidaFinal1 > vidaFinal2:
        lista.remove(pokemon2)

        print("\nGANADOR:")
        print("Entrenador:", entrenador1)
        print("Pokemon:", nombre1)

    elif vidaFinal2 > vidaFinal1:
        lista.remove(pokemon1)

        print("\nGANADOR:")
        print("Entrenador:", entrenador2)
        print("Pokemon:", nombre2)

    else:
        lista.remove(pokemon1)
        lista.remove(pokemon2)

        print("\nAMBOS PERDIERON.")


def menu():
    lista = []

    while True:
        print("\n==============================")
        print("          MENU POKEMON")
        print("==============================")
        print("1. Crear Entrenador")
        print("2. Listar Entrenadores")
        print("3. Borrar por Pokemon")
        print("4. Pelea Pokemon")
        print("5. Fin")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            crearEntrenador(lista)

        elif opcion == "2":
            listaEntrenador(lista)

        elif opcion == "3":
            borraPorPokemon(lista)

        elif opcion == "4":
            peleaPokemon(lista)

        elif opcion == "5":
            print("Fin del programa.")
            break


# Llamada principal para iniciar el programa
menu()
