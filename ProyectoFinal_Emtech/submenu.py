def fsubmenu(a):

    flag_opc = 0

    if a == 1:
        limpiarPantalla = '\n' * 20

        dialog = [
            """          ************ SubMenú *************
            Productos más vendidos y rezagados
        """,
        '               Top 5 productos más vendidos',
        '               Top 10 productos más buscados',
        '   Los 5 productos con menores ventas (por categoría)',
        '   Los 10 productos con menores busquedas por categoría']

        separado = ['⥼', '⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯', '⥽']
        separador = separado[0] + separado[1] + separado[2]

        opciones =['Top 5 productos más vendidos', 'Top 10 productos más buscados', 
        'Los 5 productos con menores ventas (por categoría)', 
        'Los 10 productos con menores busquedas (por categoría)']
        opc1 = [
            '1 - Top 5 del total de ventas (comprende año 2020)',
            '2 - Top 5 por mes (año 2020)'
            ]
        opc2 = []
        opc3 = [
            '1 - Menores ventas por categoría (comprende ventas en todo el año 2020)',
            '2 - Menores ventas por mes y categoría (Ingresa el mes, por ejemplo: Febrero)'
        ]
        opc4 = []

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
            # TOP DEL TOTAL
            if seleccion == 1:
                indicacion += '¿Cómo quieres ver el top?:'
                for op in opc1:
                    if indice % 2:
                        vineta = '✦'
                    else:
                        vineta = '✧'
                    listaDeOpciones += f'{vineta}{vineta} ' + op + '\n'
                    indice += 1
                flag_opc = 1

            # TOP POR MES
            if seleccion == 2:
                indicacion = '\t'
                return 200

            # MENORES VENTAS POR CAT
            if seleccion == 3:
                indicacion = '\t'
                return 300

            # MENORES BUSQUEDAS POR CAT
            if seleccion == 4:
                indicacion = '\t?:'
                return 400
    

            # Dialogo, indicación, lista de opciones
            print(limpiarPantalla, dialog[seleccion])
            print(separador)
            print(indicacion)
            print(listaDeOpciones)
            a = f'{" " * (len(separado[1]) - 3)}'
            seleccion = input(a + '・➣ ')

            if flag_opc != 0:

                if flag_opc == 1:
                    if (seleccion == '' or seleccion is None) or seleccion not in('1', '2', '3'):
                        seleccion = 1
                    else:
                        if seleccion == '1':
                            return 101
                        elif seleccion == '2':
                            return 102
                        elif seleccion == '3':
                            return 103
            else:
                if (seleccion == '' or seleccion is None) or seleccion not in('1', '2', '3', '4'):
                    seleccion = 0
                else:
                    seleccion = int(seleccion)
                    
            meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio']
        

    elif a == 2:
        return 2000
    elif a == 3:
        return 3
