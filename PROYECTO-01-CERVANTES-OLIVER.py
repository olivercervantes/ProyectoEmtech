from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#DEFINIR USUARIOS

Usr_permitidos = ["POLO", "123"], ["JOSE", "123"], ["MARTIN", "123"]
acceso = 0

#INPUT USUARIOS

print("°°°°°°Bienvenido al sistema°°°°°°" + "\n")
usr_input = input("Ingresa el usuario: ")
contra_input = input("Ingresa la contraseña: ")

for usuario in Usr_permitidos:
    if usuario[0] == usr_input and usuario[1] == contra_input:

        acceso = 1
        break

    else:
        continue
#Acceso Inicio/Index
if acceso == 0:
    print("\n" + "\n" + "\n"
          "Lo siento, el usuario no está registrado en nuestra base de datos. "
          + "\n")

if acceso == 1:
    print("\n" "°°°°°°°Acceso correcto, bienvenido a LifeStore°°°°°°" + "\n")

    print(
        "Categorias disponibles para consulta:\n\n A.- Tops por ventas y búsquedas \n B.- Productos por reseña en el servicio \n C.- Total de ingresos por producto \n  "
    )

    opcion_seleccionada = input(
        "°°°°°Elige que categoría deseas consultar°°°°° :")

    if opcion_seleccionada == "A":
        print("\n\n\n Has seleccionado la categoría: " + opcion_seleccionada,
              "\n")
        print(
            "A.-Top producto mas vendidos \nB.- Top productos con mayor búsqueda"
            "\n"
            "C.- Top producto menos vendidos"
            "\n"
            "D.- Top productos con menor búsqueda"
            "\n")
        opcionA = input(
            "\n°°°°°¿Cuáles productos quieres ver? (A/B/C/D)°°°°° :")
        total_vendidos = []
        resultadosbusqueda = []
        contador = 0
        contadorbus = 0
        if opcionA == "A":
            print(
                "\n\n\n\n °°°°°Has seleccionado Productos más vendidos:°°°°° \n\n\n\n "
            )
            #Creacion de lista vendidos
            for producto in lifestore_products:
                for venta in lifestore_sales:
                    if producto[0] == venta[1]:
                        contador += 1
                if contador != 0:
                    vendidos = [contador, producto[1], producto[3]]
                    total_vendidos.append(vendidos)
                    contador = 0
            #OrdenarVendidos
            total_vendidos.sort(reverse=True)
            #HacerElTop
            for top42 in range(0, 42):
                print(
                    total_vendidos[top42][0],
                    "items vendidos de ",
                    total_vendidos[top42][1],
                )
            #for venta in total_vendidos:
            #print("El producto", venta[0],venta[1], "se vendió como",  )

        elif opcionA == "B":
            print(
                "\n\n\n\n °°°°°Has seleccionado PRODUCTOS CON MAYORES BÚSQUEDAS°°°°° \n\n\n\n "
            )
            print("Se han omitido productos con cero búsquedas: \n ")

            for producto in lifestore_products:
                for busquedas in lifestore_sales:
                    if producto[0] == busquedas[1]:
                        contadorbus += 1
                totales_bus = [contadorbus, producto[1]]
                resultadosbusqueda.append(totales_bus)
                contadorbus = 0
            resultadosbusqueda.sort(reverse=True)
            #no hay resultados suficientes para 100 productos, SE USAN SOLO 96
            for top in range(0, 96):
                if resultadosbusqueda[top][0] != 0:
                    print(resultadosbusqueda[top][0],
                          resultadosbusqueda[top][1])

        elif opcionA == "C":
            print(
                "\n\n\n\n °°°°°Has seleccionado productos menos vendidos°°°°° \n\n\n\n "
            )
            #Creacion de lista vendidos
            for producto in lifestore_products:
                for venta in lifestore_sales:
                    if producto[0] == venta[1]:
                        contador += 1
                if contador != 0:
                    vendidos = [contador, producto[1], producto[3]]
                    total_vendidos.append(vendidos)
                    contador = 0
            #OrdenarVendidos
            total_vendidos.sort()
            #HacerElTop
            for top42 in range(0, 42):
                print(
                    total_vendidos[top42][0],
                    "items vendidos de ",
                    total_vendidos[top42][1],
                )
        elif opcionA == "D":
            print(
                "\n\n\n\n °°°°°Has seleccionado PRODUCTOS CON MENORES BÚSQUEDAS°°°°°\n\n\n\n "
            )

            for producto in lifestore_products:
                for busquedas in lifestore_sales:
                    if producto[0] == busquedas[1]:
                        contadorbus += 1
                totales_bus = [contadorbus, producto[1]]
                resultadosbusqueda.append(totales_bus)
                contadorbus = 0
            resultadosbusqueda.sort()
            #no hay resultados suficientes para 100 productos, SE USAN SOLO 96
            for top in range(0, 96):

                print(resultadosbusqueda[top][0], resultadosbusqueda[top][1])

    elif opcion_seleccionada == "B":
        print("\n\n\n Has seleccionado la categoría: " + opcion_seleccionada)
        print("Productos por reseña en el servicio.")
        print(
            "\n\n\n\n °°°°°Has seleccionado PRODUCTOS CON MEJORES RESEÑAS°°°°°\n\n\n\n "
        )
        resenas = []
        contadorrese = 0
        for producto in lifestore_products:
            for cali in lifestore_sales:
                if producto[0] == cali[1]:
                    contadorrese += 1
            trese = [contadorrese, producto[2], cali[2], cali[4]]
            resenas.append(trese)
            contadorrese = 0
        resenas.sort()
        #no hay resultados suficientes para 100 productos, SE USAN SOLO 96
        for top in range(0, 20):
            print(resenas[top][2], resenas[top][2])

    elif opcion_seleccionada == "C":
        print("\n\n\n Has seleccionado la categoría: " + opcion_seleccionada)
        print("Total de ingresos por producto")
        ventast = []
        contador = 0
        for producto in lifestore_products:
            for ventat in lifestore_sales:
                if producto[0] == ventat[1]:
                    contador += 1
            resultado = [contador * producto[2], producto[1]]
            ventast.append(resultado)
            contador = 0
            ventast.sort(reverse=True)

        suma_anual = 0
        for top in range(0, 100):
            print(
                "$",
                (ventast[top][0]),
                " DE ",
                ventast[top][1],
            )
