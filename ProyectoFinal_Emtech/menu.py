def fmenu():
    limpiarPantalla = '\n' * 20

    dialog = [
        """        
     **************************************
     *********** MENÚ PRINCIPAL ***********
     **************************************

             * LIFESTORE REPORTES *
    """,
    'PRODUCTOS MÁS VENDIDOS Y PRODUCTOS REZAGADOS', 
    'PRODUCTOS POR RESEÑA EN EL SERVICIO',
    '',
    '']

    separado = ['⥼', '⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯', '⥽']
    separador = separado[0] + separado[1] + separado[2]

    opciones =['PRODUCTOS MÁS VENDIDOS Y PRODUCTOS REZAGADOS', 'PRODUCTOS POR RESEÑA EN EL SERVICIO',
     'TOTAL DE INGRESOS Y VENTAS PROMEDIO MENSUALES', 'Salir del Sistema']

    #   FUNCIONAL

    seleccion = 0
    while True:
        listaDeOpciones = ''
        indice = 1
        indicacion = ' '
        
        # Menu principal
        if seleccion == 0:
            indicacion += 'Ir a:'
            for opcion in opciones:
                if indice % 2:
                    vineta = '•'
                else:
                    vineta = '•'
                listaDeOpciones += f'{vineta}{indice}{vineta} ' + opcion + '\n'
                indice += 1
        
        # SubMenú 1 Productos más vendidos
        if seleccion == 1:
            indicacion += 'Productos más vendidos:'
            return 1
        
        # SubMenú 2 Productos por reseña
        if seleccion == 2:
            # listaDeOpciones = ''
            # indice = 1
            indicacion = '\tProductos por reseña:'
            return 2
        
        # No hay submenú
        if seleccion == 3:
            indicacion = '\tTotal ingresos:'
            return 3

        #Playlists
        if seleccion == 4:
            # listaDeOpciones = ''
            # indice = 1
            indicacion = '\tDe qué humor estás hoy?:'
            return 4

        # Dialogo, indicación, lista de opciones
        print(limpiarPantalla, dialog[seleccion])
        print(separador)
        print(indicacion)
        print(listaDeOpciones)
        a = f'{" " * (len(separado[1]) - 35)}'
        print(separador)
        seleccion = input(a + 'Ingresa el número de la opción ・➣  ')

        if (seleccion == '' or seleccion is None) or seleccion not in('1', '2', '3', '4'):
            return 'e'
        else:
            return int(seleccion)
        """if seleccion == 'e':
            break
        seleccion = int(seleccion)"""