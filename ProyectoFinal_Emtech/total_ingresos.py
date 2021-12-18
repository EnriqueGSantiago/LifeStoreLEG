from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
from operator import itemgetter
"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
                    0           1           2                  3        4
lifestore_products = [id_product, name, price, category, stock]
"""
def ftotalingresos():
    # Ventas Validas
    ventas = []
    # lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    for sale in lifestore_sales:
        # refund = sale[-1]
        refund = sale[4]
        if refund == 1:
            continue
        else:
            ventas.append(sale)
    meses = [
        '/01/', '/02/', '/03/', '/04/', '/05/', '/06/',
        '/07/', '/08/', '/09/', '/10/', '/11/', '/12/'
        ]

    ventas_por_mes = []
    for mes in meses:
        lista_vacia = []
        ventas_por_mes.append(lista_vacia)

    #print(ventas_por_mes)

    for venta in ventas:
        # Datos de la venta
        id_venta = venta[0]
        fecha = venta[3]
        # Clasificar en mes
        # Comienzo en el mes 0 ('/01/')
        contador_de_mes = 0

        for mes in meses:
            if mes in fecha:
                ventas_por_mes[contador_de_mes].append(id_venta)
                continue
            contador_de_mes = contador_de_mes + 1 
    #print(ventas_por_mes)

    ganancias_mensuales = []
    for venta_mensual in ventas_por_mes:
        ganancia_del_mes = 0
        contador_productos_mes = 0
        #print(gancias_mensuales)
        for id_venta in venta_mensual:
            indice_de_venta = id_venta - 1
            info_de_venta = lifestore_sales[indice_de_venta]
            id_prod = info_de_venta[1]
            indice_de_prod = id_prod - 1
            info_del_prod = lifestore_products[indice_de_prod]
            precio_de_prod = info_del_prod[2]
            ganancia_del_mes = ganancia_del_mes + precio_de_prod
            contador_productos_mes = contador_productos_mes + 1
        ganancias_mensuales.append([ganancia_del_mes,contador_productos_mes])
    #print(ganancias_mensuales)

    meses_desc = [
        '    Enero', '  Febrero', '    Marzo', '    Abril', '     Mayo', '    Junio',
        '    Julio', '    Agosto', 'Septiembre', '   Octubre', ' Noviembre', ' Diciembre'
        ]
    meses_dia = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    espaciado_num = ['          ','           ', '            ', '                ']

    limpiarPantalla = '\n' * 20
    print(limpiarPantalla)
    print('          Reporte Mensual de Ventas 2020')
    print('****************************************************')
    print('Meses     | Cantidad Prod | Promedio diario | Total')
    print('____________________________________________________')
    print('\n')
    i_mes = 0
    for mes_desc in meses_desc:
        if ganancias_mensuales[i_mes][0]/meses_dia[i_mes] >= 1000:
            print(mes_desc + '        ' + str(ganancias_mensuales[i_mes][1]) + '          ' + str(round(ganancias_mensuales[i_mes][0]/meses_dia[i_mes], 1)) 
            +  espaciado_num[0] + str(ganancias_mensuales[i_mes][0]))
            i_mes += 1
        elif ganancias_mensuales[i_mes][0]/meses_dia[i_mes] > 100 and ganancias_mensuales[i_mes][0]/meses_dia[i_mes] < 1000: #and ganancias_mensuales[i_mes][0]/meses_dia[i_mes] > 0 :
            print(mes_desc + '        ' + str(ganancias_mensuales[i_mes][1]) + '          ' + str(round(ganancias_mensuales[i_mes][0]/meses_dia[i_mes], 1)) 
            +  espaciado_num[1] + str(ganancias_mensuales[i_mes][0]))
            i_mes += 1
        elif ganancias_mensuales[i_mes][0]/meses_dia[i_mes] < 100 and ganancias_mensuales[i_mes][0]/meses_dia[i_mes] > 0:
            print(mes_desc + '        ' + str(ganancias_mensuales[i_mes][1]) + '          ' + str(round(ganancias_mensuales[i_mes][0]/meses_dia[i_mes], 1)) 
            +  espaciado_num[2] + str(ganancias_mensuales[i_mes][0]))
            i_mes += 1
        elif ganancias_mensuales[i_mes][0]/meses_dia[i_mes] == 0:
            print(mes_desc + '        ' + str(ganancias_mensuales[i_mes][1]) + '          ' + str(round(ganancias_mensuales[i_mes][0]/meses_dia[i_mes], 1)) 
            +  espaciado_num[3] + str(ganancias_mensuales[i_mes][0]))
            i_mes += 1
    print('____________________________________________________')
    print('\n')
    retro = input(" PARA CERRAR SESIÓN PRESIONE CUALQUIER TECLA, SI DESEA REALIZAR OTRA CONSULTA PRESIONE 'Y': ")
    return retro