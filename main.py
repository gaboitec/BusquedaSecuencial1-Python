def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

cantidad = int(input("¿Cuantso repartidores participaron?: "))

repartidores = {}

for i in range(cantidad):
    nombre = input(f"Nombre del repartidor {i + 1}: ")

    if nombre not in repartidores:
        while True:
            try:
                paquetes = int(input("  Cantidad de paquetes entregados: "))
                if paquetes >= 0:
                    break
            except ValueError:
                print("  Ingresa un número válido para la cantidad de paquetes.")

        while True:
            zona = input("  Zona asignada: ")
            if zona != "":
                break
            else:
                print("  La zona no puede estar vacía.")

        repartidores[nombre] = {
            "paquetes": paquetes,
            "zona": zona
        }
    else:
        print(f"  El repartidor {nombre} ya está registrado.")


print("\nCANTIDAD DE REPARTIDORES: ", len(repartidores))
for nombre, datos in repartidores.items():
    print(f"Repartidor: {nombre}    Paquetes: {datos['paquetes']}    Zona: {datos['zona']}")


print("\nRANKING POR CANTIDAD DE PAQUETES:")
listaRepartidores = [repartidores.values()]
repartidores_ordenados = quick_sort(listaRepartidores)

for datos in repartidores_ordenados:
    print(f"{} - {datos['paquetes']} paquetes - Zona {datos['zona']}")


print("\nBUSCAR REPARTIDOR")
while True:
    nombre_buscar = input("Ingrese el nombre del repartidor a buscar: ")

    if nombre_buscar in repartidores:
        print(f"{nombre_buscar} entregó {repartidores[nombre_buscar]['paquetes']} paquetes en la zona {repartidores[nombre_buscar]['zona']}.")
        break
    else:
        print(f"El repartidor {nombre_buscar} no está registrado.")


print("\nESTADISTICAS DE REPARTIDORES")
